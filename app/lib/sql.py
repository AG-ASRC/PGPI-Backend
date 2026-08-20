from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.lib.env import getEnvByKey   

DATABASE_URL = getEnvByKey(key="DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def dbInstance():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

Base = declarative_base()