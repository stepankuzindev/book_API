from sqlalchemy import DATE, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

book_m2m_author = Table(
    "book_m2m_author",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("books_id", Integer, ForeignKey("books.id")),
    Column("authors_id", Integer, ForeignKey("authors.id")),
)

book_m2m_order = Table(
    "book_m2m_order",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("books_id", Integer, ForeignKey("books.id")),
    Column("orders_id", Integer, ForeignKey("orders.id")),
)


class Book(Base):
    """
    models.Book(name="Book 1", pub_date=datetime.now())
    db_authors = db.query(models.Author).filter(models.Author.id.in_([1,2])).all()
    for db_author in db_authors:
        db_book.authors.append(db_author)

    models.Book(name="Book 2", pub_date=datetime.now())
    db_author = db.query(models.Author).get(1)
    db_book.authors.append(db_author)
    """

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pub_date = Column(DATE)
    authors = relationship("Author", secondary=book_m2m_author, backref="books")


class Author(Base):
    """
    models.Author(name="Author 1")
    models.Author(name="Author 2")
    """

    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Staff(Base):
    """
    models.Staff(name="Manager")
    models.Staff(name="Salesman")
    """

    __tablename__ = "staffs"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class User(Base):
    """
    models.User(name="User 1")

    db_user = models.User(name="Staff 1")
    db_staff = db.query(models.Staff).get(1)
    db_user.staff.append(db_user)
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    staff_id = Column(Integer, ForeignKey("staffs.id"))
    staff = relationship("Staff")


class Order(Base):
    """
    db_order = models.Order(user_id=1)

    db_books = db.query(models.Book).filter(models.Book.id.in_([1,2])).all()
    for db_book in db_books:
        db_order.books.append(db_book)
    """

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
    books = relationship("Book", secondary=book_m2m_order, backref="orders")
