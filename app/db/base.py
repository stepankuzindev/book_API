# Import all the models, so that Base has them before being
# imported by Alembic
from typing import Any

from sqlalchemy import exc

from app.db.base_class import Base  # noqa
from app.models.models import Author  # noqa


def save(db: Any, object: Any) -> None:
    try:
        db.add(object)
        db.commit()
        db.refresh(object)
    except exc.SQLAlchemyError as e:
        raise e


def delete(db: Any, object: Any) -> None:
    try:
        db.delete(object)
        db.commit()
    except exc.SQLAlchemyError as e:
        raise e


def update(db: Any) -> None:
    try:
        db.commit()
    except exc.SQLAlchemyError as e:
        raise e
