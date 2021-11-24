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


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pub_date = Column(DATE)
    authors = relationship("Author", secondary=book_m2m_author, backref="books")

    def __repr__(self):
        return self.name


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return self.name
