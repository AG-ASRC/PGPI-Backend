# PGPI-Backend
Backend de la solution PGPI (Plateforme de Gestion et de Pilotage d'Infrastructure)

## Architecture

La structure du projet, le flux d'une requete et la relation entre FastAPI,
Pydantic, SQLAlchemy et Alembic sont decrits dans la
[documentation d'architecture](docs/architecture.md).

## Documentation

La documentation du projet est disponible dans le dossier `docs/` :

- [Architecture et persistance](docs/architecture.md) : relation entre
	Pydantic, SQLAlchemy et Alembic, organisation des ressources et procedure de
	migration.
- [Exemple de ressource custom](docs/customs-ressources-example/) : structure
  d'une ressource avec schemas Pydantic, modeles SQLAlchemy et routes FastAPI.
- [Environnement de developpement](docs/environnement.md) : creation du venv,
	activation et installation des dependances.
- [Lancer l'API avec Uvicorn](docs/uvicorn.md) : demarrage du serveur et acces
	a la documentation interactive.
- [Gerer les migrations avec Alembic](docs/alembic.md) : creation, application,
	consultation et annulation des migrations.
- [Creer un module custom](docs/creation-module-custom.md) : structure des
  dossiers, schemas Pydantic, modeles SQLAlchemy et routes FastAPI.

Pour ajouter une nouvelle ressource, creer un dossier dans `app/customs/` et
suivre la structure de l'exemple ainsi que les etapes decrites dans la
documentation d'architecture.

## Demarrage rapide

1. Suivre le guide [Environnement de developpement](docs/environnement.md).
2. Lancer l'API avec le guide [Uvicorn](docs/uvicorn.md).
3. Initialiser la base avec le guide [Alembic](docs/alembic.md).
