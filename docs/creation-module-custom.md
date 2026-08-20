# Creer un module custom

Ce guide explique comment ajouter une nouvelle ressource metier dans
`app/customs/`. Les modules customs sont charges automatiquement par
`app/lib/autoloader.py`.

## Structure d'un module

Remplacer `<ressource>` par un nom Python en minuscules, sans espace ni tiret.
Par exemple, pour une ressource `project` :

```text
app/
└── customs/
    └── project/
        ├── models/
        │   ├── __init__.py
        │   └── project.py
        ├── schemas/
        │   ├── __init__.py
        │   └── project.py
        └── routes/
            ├── __init__.py
            └── project.py
```

Le package `routes/` est importe par l'autoloader comme le module principal des
routes. Son fichier `__init__.py` doit donc reexporter les routeurs :

```python
from .project import routers
```

## 1. Initialiser le module

Fichier : `app/customs/project/__init__.py`

Ce fichier indique que `project` est un package Python :

```python
"""Ressource project."""
```

## 2. Creer le modele SQLAlchemy

Fichier : `app/customs/project/models/project.py`

Le modele represente la table en base. La fonction `to_dict` est un exemple de
fonction utilitaire pour convertir une instance en dictionnaire :

```python
from sqlalchemy import Column, Integer, String

from app.lib.sql import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
```

Le modele doit etre importe par `alembic/env.py` pour que sa table soit
presente dans `Base.metadata` lors de l'autogeneration d'une migration.

## 3. Creer les schemas Pydantic

Fichier : `app/customs/project/schemas/project.py`

Les schemas definissent le contrat de l'API. La methode `as_payload` est un
exemple de fonction permettant de recuperer les donnees validees :

```python
from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

    def as_payload(self) -> dict:
        return self.model_dump()


class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        from_attributes = True
```

Le schema d'entree ne doit pas etre remplace par le modele SQLAlchemy : ils
repondent a deux besoins differents.

## 4. Creer les routes FastAPI

Fichier : `app/customs/project/routes/project.py`

Le routeur valide les donnees avec Pydantic, utilise la session SQLAlchemy et
retourne une reponse conforme au schema :

```python
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.lib.sql import dbInstance
from app.customs.<project>.models.project import Project
from app.customs.<project>.schemas.project import ProjectCreate, ProjectResponse


router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(dbInstance),
) -> Project:
    project = Project(**project_data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


routers = [router]
```

La variable `routers` est necessaire car l'autoloader parcourt les routeurs
exposes par `routes.py` et les ajoute a l'application FastAPI.

## 5. Rendre les imports disponibles

Ajouter les reexports suivants :

Fichier : `app/customs/project/models/__init__.py`

```python
from .project import Project

__all__ = ["Project"]
```

Fichier : `app/customs/project/schemas/__init__.py`

```python
from .project import ProjectCreate, ProjectResponse

__all__ = ["ProjectCreate", "ProjectResponse"]
```

Fichier : `app/customs/project/routes/__init__.py`

```python
from .project import router, routers

__all__ = ["router", "routers"]
```

## 6. Enregistrer le modele dans Alembic

Dans `alembic/env.py`, importer le modele :

```python
from app.customs.project.models.project import Project
```

Cela permet a Alembic de detecter la table `projects` avec
`Base.metadata`.

## 7. Generer et appliquer la migration

Depuis la racine du projet :

```powershell
alembic revision --autogenerate -m "create projects table"
alembic upgrade head
```

Relire la migration generee avant de l'appliquer, notamment pour les colonnes
non nullables, les renommages et les suppressions de donnees.

## Checklist

- [ ] Le dossier de ressource est dans `app/customs/<ressource>/`.
- [ ] Les modeles SQLAlchemy sont dans `models/`.
- [ ] Les schemas Pydantic sont dans `schemas/`.
- [ ] Les routes sont dans `routes/` et exposent `routers`.
- [ ] Le modele est importe dans `alembic/env.py`.
- [ ] La migration a ete relue puis appliquee.
