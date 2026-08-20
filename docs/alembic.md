# Gerer les migrations avec Alembic

## Prerequis

Executer les commandes depuis la racine du projet, avec l'environnement virtuel
active et un fichier `.env` contenant notamment `DATABASE_URL`.

## Appliquer les migrations

Appliquer toutes les migrations jusqu'a la derniere version :

```powershell
alembic upgrade head
```

## Creer une migration

Apres avoir modifie ou ajoute un modele SQLAlchemy dans `app/customs/<project>/models/` ou
`app/modules/<project>/models/`, importer le modele dans `alembic/env.py` afin qu'il soit
present dans `Base.metadata`.

Generer ensuite une migration :

```powershell
alembic revision --autogenerate -m "describe the schema change"
```

Relire le fichier genere dans `alembic/versions/` avant de l'appliquer :

```powershell
alembic upgrade head
```

L'autogeneration ne comprend pas toujours les renommages, les transformations
de donnees ou les changements de contraintes. Ces operations doivent etre
verifiees et completees manuellement si necessaire.

## Consulter l'etat des migrations

Afficher la version actuellement appliquee :

```powershell
alembic current
```

Afficher l'historique des migrations :

```powershell
alembic history
```

## Revenir en arriere

Revenir a la migration precedente :

```powershell
alembic downgrade -1
```

Revenir a une revision precise :

```powershell
alembic downgrade <revision>
```

Une migration deja appliquee dans un environnement partage ne doit pas etre
modifiee. Il faut creer une nouvelle migration corrective.
