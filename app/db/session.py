from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.settings.settings import settings

engine = create_engine(settings.POSTGRES_URL, pool_pre_ping=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db: Optional[Session] = None
    try:
        db = session()
        yield db
    finally:
        if db is not None:
            db.close()
