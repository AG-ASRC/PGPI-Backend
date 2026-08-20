# Architecture et persistance

## Objectif

Cette page decrit la relation entre FastAPI, Pydantic, SQLAlchemy et Alembic
pour aider un nouveau contributeur a comprendre le projet et a faire evoluer
le modele de donnees sans casser le flux de l'API.

## Arborescence du projet

L'arborescence suivante presente l'organisation generale du projet. Le contenu
des dossiers `app/customs/` et `app/modules/` n'est pas detaille afin de garder
une vue independante des ressources et des modules metier qu'ils contiennent.

```text
PGPI-Backend/
├── app/
│   ├── customs/              # Ressources metier
│   ├── lib/                  # Utilitaires et services partages
│   └── modules/              # Modules applicatifs
├── alembic/
│   ├── versions/             # Historique des migrations
│   ├── env.py                # Configuration Alembic
│   ├── README                 # Informations Alembic
│   └── script.py.mako        # Template des migrations
├── docs/
│   ├── architecture.md      # Architecture du projet
│   ├── alembic.md            # Guide des migrations
│   ├── creation-module-custom.md # Creation d'un module custom
│   ├── environnement.md     # Guide de l'environnement virtuel
│   ├── uvicorn.md           # Guide de lancement de l'API
│   └── customs-ressources-example/ # Exemple de ressource
├── main.py                   # Point d'entree de l'API FastAPI
├── alembic.ini               # Configuration principale d'Alembic
├── requirements.txt          # Dependances Python
├── template-env.txt          # Modele des variables d'environnement
├── README.md                 # Presentation du projet
└── LICENSE                   # Licence du projet
```

## Responsabilites

| Composant | Emplacement | Responsabilite |
| --- | --- | --- |
| FastAPI | `main.py` | Expose les routes HTTP et orchestre les dependances. |
| Pydantic | `app/customs/<ressource>/schemas/` et `app/modules/<module>/schemas/` | Valide et structure les donnees des requetes et des reponses. |
| SQLAlchemy | `app/customs/<ressource>/models/`, `app/modules/<module>/models/` et `app/lib/sql.py` | Definit les tables, les relations et l'acces a la base de donnees. |
| Alembic | `alembic/` | Versionne et applique les changements du schema de la base. |

## Relation entre les composants

Pydantic et SQLAlchemy ne representent pas la meme chose :

- Un schema **Pydantic** represente le contrat de l'API. Il decrit les donnees
  qu'un client est autorise a envoyer ou a recevoir.
- Un modele **SQLAlchemy** represente la structure persistante. Il decrit la
  table, ses colonnes, ses contraintes et ses relations en base.
- **Alembic** compare l'evolution des modeles SQLAlchemy avec le schema de la
  base et conserve ces changements sous forme de migrations versionnees.

Le flux de creation d'une ressource est le suivant :

```text
                             Client HTTP
                                 |
                                 v
                    `main.py` initialise FastAPI
                                 |
                                 v
             `app/lib/autoloader.py` decouvre les routes
                                 |
                                 v
            +--------------------+--------------------+
            |                                         |
    app/customs/<ressource>/routes          app/modules/<module>/routes/
            |                                         |                              
            +--------------------+--------------------+
                                 |
                                 v
                            Schema Pydantic
                    Validation et conversion des donnees
                                 |
                                 v
                            Modele SQLAlchemy
                    Construction de l'objet a persister
                                 |
                                 v
                    Session SQLAlchemy (`app/lib/sql.py`)
                                 |
                                 v
                           Base de donnees
```

Pour creer un module custom, consulter le guide
[creation-module-custom.md](creation-module-custom.md). Il contient la
structure des dossiers, les fonctions exemples et les etapes Alembic.

Les migrations Alembic ne sont pas executees a chaque requete. Elles sont
executees lors du deploiement ou d'une operation de maintenance :

```text
Modification d'un modele SQLAlchemy
    |
    v
Migration Alembic dans `alembic/versions/`
    |
    v
`alembic upgrade head`
    |
    v
Schema de base mis a jour
```

## Faire evoluer une ressource

Lorsqu'une nouvelle propriete est necessaire, suivre cet ordre :

1. Suivre le guide [creation-module-custom.md](creation-module-custom.md).
2. Importer le modele dans `alembic/env.py`.
3. Creer une migration Alembic pour refleter le changement en base.
4. Appliquer la migration avec `alembic upgrade head`.
5. Adapter la route et les tests si le contrat de l'API change.

Exemple de commande pour generer une migration apres modification d'un modele :

```powershell
alembic revision --autogenerate -m "add field to test"
alembic upgrade head
```

La migration generee doit toujours etre relue avant execution. Il faut
notamment verifier les valeurs par defaut, les colonnes non-nullables, les
renommages de colonnes et les suppressions de donnees.

## Regles de maintenance

- Garder les schemas Pydantic independants des modeles SQLAlchemy afin de ne
  pas exposer directement la structure interne de la base.
- Importer les modeles dans `alembic/env.py` afin qu'ils soient presents dans
  `Base.metadata` lors de l'autogeneration.
- Ne pas modifier une migration deja appliquee en environnement partage ;
  creer une nouvelle migration corrective.
- Tester une migration sur une copie de la base avant de la deployer.
- Documenter dans la migration les transformations de donnees qui ne peuvent
  pas etre deduites automatiquement.
