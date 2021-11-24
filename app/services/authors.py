import app.db.base as models
from app.db.base import db
from app.schemas.authors import AuthorListResponseSchema, AuthorResponseSchema


def get_authors() -> AuthorListResponseSchema:
    authors = db.query(models.Author).all()

    return AuthorListResponseSchema().dump({"authors": authors})


def add_author(name: str) -> AuthorResponseSchema:
    db_author = models.Author(name=name)
    models.save(db=db, object=db_author)

    return AuthorResponseSchema().dump(db_author)
