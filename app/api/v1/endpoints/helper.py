from datetime import datetime

import app.models.models as models
from app.db.base import db, save
from app.main import app


@app.route("/api/v1/helper", methods=["POST"])
def helper() -> {}:
    """
    ---
    post:
        description: Helper
    """

    # Author
    db_author = models.Author(name="Author 1")
    save(db=db, object=db_author)

    db_author = models.Author(name="Author 2")
    save(db=db, object=db_author)

    # Book
    db_book = models.Book(name="Book 1", pub_date=datetime.now())
    db_authors = db.query(models.Author).filter(models.Author.id.in_([1, 2])).all()
    for db_author in db_authors:
        db_book.authors.append(db_author)
    save(db=db, object=db_book)

    db_book = models.Book(name="Book 2", pub_date=datetime.now())
    db_author = db.query(models.Author).get(1)
    db_book.authors.append(db_author)
    save(db=db, object=db_book)

    # Staff
    db_staff = models.Staff(name="Manager")
    save(db=db, object=db_staff)

    db_staff = models.Staff(name="Salesman")
    save(db=db, object=db_staff)

    # User
    db_user = models.User(name="User 1")
    save(db=db, object=db_user)

    db_user = models.User(name="Staff 1")
    db_user.staff_id = 1
    save(db=db, object=db_user)

    # Order
    db_order = models.Order(user_id=1)
    db_books = db.query(models.Book).filter(models.Book.id.in_([1, 2])).all()
    for db_book in db_books:
        db_order.books.append(db_book)
    save(db=db, object=db_order)

    return {}
