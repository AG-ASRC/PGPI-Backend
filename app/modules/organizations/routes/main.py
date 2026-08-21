from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.lib.sql import dbInstance
from app.modules.organizations.schemas.main import OrganizationResponse, Organization
from app.modules.organizations.repositories.main import getAllOrganizations, getOrganizationByKey, createOrganization, updateOrganization

router = APIRouter(tags=["organization"])

@router.get("/organizations",
            summary="Get All Organizations",
            response_model=list[OrganizationResponse])
def organization(db : Session = Depends(dbInstance)):
    return getAllOrganizations(sql=db)

@router.get("/organization/{organization_key}",
            summary="Get Information about a specific Organization by id",
            response_model=OrganizationResponse)
def organization(organization_key : int|UUID, db : Session = Depends(dbInstance)):

    res = getOrganizationByKey(key=organization_key, sql=db)
    return res

@router.post("/organization",
             summary="Create new Organization",
             response_model=Organization)
def organization(org : Organization, db : Session = Depends(dbInstance)):
    return createOrganization(data=org, sql=db)

@router.put("/organization/{organization_key}",
            summary="Update Information about a specific Organization by id",
            response_model=OrganizationResponse)
def organization(organization_key: int |UUID, org : Organization, db : Session = Depends(dbInstance)):
    return updateOrganization(key=organization_key,data=org, sql=db)