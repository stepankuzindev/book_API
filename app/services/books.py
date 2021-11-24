from datetime import datetime

import app.db.base as models
from app.db.base import db
from app.schemas.books import BookListResponseSchema, BookResponseSchema


def get_books() -> BookListResponseSchema:
    books = db.query(models.Book).all()

    return BookListResponseSchema().dump({"books": books})


def add_book(name: str, pub_date: datetime, author_ids: list) -> BookResponseSchema:
    db_book = models.Book(name=name, pub_date=pub_date)

    db_authors = db.query(models.Author).filter(models.Author.id.in_(author_ids)).all()
    for db_author in db_authors:
        db_book.authors.append(db_author)

    models.save(db=db, object=db_book)

    return BookResponseSchema().dump(db_book)
