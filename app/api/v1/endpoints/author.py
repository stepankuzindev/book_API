from flask import Flask

import app.services.authors as services
from app.main import app


@app.route("/api/v1/authors", methods=["GET"])
def get_authors() -> Flask.response_class:
    """Get List of Authors
    ---
    get:
        description: Get List of Authors
        responses:
            200:
                description: Return a authors list
                content:
                    application/json:
                        schema: AuthorListResponseSchema
    """

    return services.get_authors()


@app.route("/api/v1/authors", methods=["POST"])
def add_author(
    name: str = "Author 1",
) -> Flask.response_class:
    """Add Author
    ---
    post:
        description: Add Author
        parameters: [
          {
            "name": "name",
            "default": "Author 1",
            "format": "string",
            "in": "query",
            "required": true,
            "type": "string"
          }
        ]
        responses:
            200:
                description: Return a author
                content:
                    application/json:
                        schema: AuthorResponseSchema
    """

    return services.add_author(name=name)
