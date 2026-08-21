# PGPI-Backend
Backend de la solution PGPI (Plateforme de Gestion et de Pilotage d'Infrastructure)

## Vue d'ensemble

Ce projet expose une API FastAPI qui automatise le chargement des modules via
l'autoloader present dans [app/lib/autoloader.py](app/lib/autoloader.py). Les
modules metiers sont organises dans [app/modules](app/modules), avec des sous-
structures de schemas, repositories, routes et modeles.

## Fonctionnalites actuelles

### Module organizations

Le module [app/modules/organizations](app/modules/organizations) contient la
gestion des organisations avec les operations suivantes :

- Recuperation de toutes les organisations
- Recuperation d'une organisation par id ou UUID
- Creation d'une organisation
- Mise a jour d'une organisation

Les routes exposees sont detaillees dans [docs/API.md](docs/API.md).

## Architecture

Le projet s'appuie sur :

- FastAPI pour l'API HTTP et les routes
- Pydantic pour la validation des donnees
- SQLAlchemy pour la couche ORM et la base de donnees
- Alembic pour les migrations de schema

La documentation technique est disponible dans le dossier [docs](docs) :

- [docs/API.md](docs/API.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/environnement.md](docs/environnement.md)
- [docs/uvicorn.md](docs/uvicorn.md)
- [docs/alembic.md](docs/alembic.md)
- [docs/creation-module-custom.md](docs/creation-module-custom.md)

## Demarrage rapide

1. Creer et activer un environnement virtuel selon le guide
   [docs/environnement.md](docs/environnement.md).
2. Installer les dependances :

```bash
pip install -r requirements.txt
```

3. Lancer le serveur :

```bash
uvicorn main:app --reload
```

4. Appliquer les migrations Alembic si besoin :

```bash
alembic upgrade head
```

## Notes de developpement

- Les modules sont charges automatiquement par [app/lib/autoloader.py](app/lib/autoloader.py).
- Les sessions SQLAlchemy sont centralisees dans [app/lib/sql.py](app/lib/sql.py).
- Les variables d'environnement sont chargees depuis le fichier `.env` dans
  [app/lib/env.py](app/lib/env.py).
