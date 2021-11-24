from flask import Flask

import app.services.orders as services
from app.main import app


@app.route("/api/v1/orders", methods=["POST"])
def create_order(
    user_id: int = 1,
    book_ids: list = [1, 2],
) -> Flask.response_class:
    """
    ---
    post:
        description: Create_order
        parameters: [
          {
            "name": "user_id",
            "default": "1",
            "format": "int",
            "in": "query",
            "required": true,
            "type": "int"
          },
          {
            "name": "book_ids",
            "default": "[1, 2]",
            "format": "list",
            "in": "query",
            "required": true,
            "type": "list"
          }
        ]
        responses:
            200:
                description: Return a order
                content:
                    application/json:
                        schema: OrderResponseSchema
    """

    return services.create_order(user_id=user_id, book_ids=book_ids)
