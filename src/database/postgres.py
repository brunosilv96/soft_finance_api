import os
from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlmodel import SQLModel
from src.core.settings import settings

engine = create_engine(str(settings.DATABASE_URL), echo=True)


def postgres_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
