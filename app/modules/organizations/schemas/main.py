from uuid import UUID
from pydantic import BaseModel

class OrganizationResponse(BaseModel):
    id: int
    uuid: UUID
    name: str
    company_name: str
    city: str
    postal_code: str
    street: str
    country: str
    latitude: float
    longitude: float

class Organization(BaseModel):
    name: str
    company_name: str
    city: str
    postal_code: str
    street: str
    country: str
    latitude: float
    longitude: float