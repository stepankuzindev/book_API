import app.db.base as models
from app.db.base import db
from app.schemas.orders import OrderResponseSchema


def create_order(
    user_id: int,
    book_ids: list,
) -> OrderResponseSchema:
    db_order = models.Order(user_id=user_id)

    db_books = db.query(models.Book).filter(models.Book.id.in_(book_ids)).all()
    for db_book in db_books:
        db_order.books.append(db_book)

    models.save(db=db, object=db_order)

    return OrderResponseSchema().dump(db_order)
