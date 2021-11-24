from datetime import datetime

from flask import Flask

import app.services.books as services
from app.main import app


@app.route("/api/v1/books", methods=["GET"])
def get_books() -> Flask.response_class:
    """Get List of books
    ---
    get:
        description: Get List of Books
        responses:
            200:
                description: Return a books list
                content:
                    application/json:
                        schema: BookListResponseSchema
    """

    return services.get_books()


@app.route("/api/v1/books", methods=["POST"])
def add_book(
    name: str = "Book 1", author_ids: list = [1, 2], pub_date: datetime = datetime.now()
) -> Flask.response_class:
    """Add Author
    ---
    post:
        description: Add book
        parameters: [
          {
            "name": "name",
            "default": "Book 1",
            "format": "string",
            "in": "query",
            "required": true,
            "type": "string"
          },
          {
            "name": "author_ids",
            "default": "[1, 2]",
            "format": "list",
            "in": "query",
            "required": true,
            "type": "list"
          },
          {
            "name": "pub_date",
            "format": "string",
            "in": "query",
            "required": false,
            "type": "string"
          }
        ]
        responses:
            200:
                description: Return a book
                content:
                    application/json:
                        schema: BookResponseSchema
    """

    return services.add_book(name=name, pub_date=pub_date, author_ids=author_ids)
