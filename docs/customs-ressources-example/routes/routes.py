from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.lib.sql import dbInstance
from app.custom.models import Project
from app.custom.schemas import ProjectCreate, ProjectResponse


router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(dbInstance),
) -> Project:
    project = Project(
        name=project_data.name,
        description=project_data.description,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(dbInstance)) -> Project:
    return db.query(Project).filter(Project.id == project_id).first()
