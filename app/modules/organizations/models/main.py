from sqlalchemy import Column, Integer, String, UUID, Float
import uuid

from app.lib.sql import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID, index=True,unique=True, nullable=False, default=uuid.uuid4)
    name = Column(String(255), index=True, nullable=False)
    company_name = Column(String(255), index=True, nullable=False)
    city = Column(String(255), index=True, nullable=False)
    postal_code = Column(String(10), index=True, nullable=False)
    street = Column(String(255), index=True, nullable=False)
    country = Column(String(255), index=True, nullable=False)
    latitude = (Column(Float, nullable=False))
    longitude = (Column(Float, nullable=False))
