from uuid import UUID

from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from app.modules.organizations.schemas.main import Organization
from app.modules.organizations.models.main import Organization

def getAllOrganizations(sql : Session) -> list[Organization]:
    query = select(Organization)
    return sql.scalars(query).all()

def getOrganizationByKey(key : str | UUID, sql : Session):

    query = select(Organization).where(
        or_(
            Organization.id == key,
            Organization.uuid == key,
        )
    )

    return sql.scalars(query).first()


def createOrganization(data : Organization, sql : Session) -> Organization:
    organization = Organization(
        name=data.name,
        company_name=data.company_name,
        city=data.city,
        postal_code=data.postal_code,
        street=data.street,
        country=data.country,
        latitude=data.latitude,
        longitude=data.longitude,
    )

    sql.add(organization)
    sql.commit()
    sql.refresh(organization)

    return organization

def updateOrganization(key: int|UUID, data : Organization, sql : Session) -> Organization:

    organization = sql.get(Organization, key)

    if organization is None:
        raise ValueError(f"Organization with key : '{key}' doesn't exists")

    for key, value in data.model_dump().items():
        setattr(organization, key, value)

    sql.commit()
    sql.refresh(organization)

    return organization