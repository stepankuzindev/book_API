from flask import Flask

import app.services.todo as services
from app.main import app


@app.route("/api/v1/todo", methods=["GET"])
def todo() -> Flask.response_class:
    """Get List of Todo
    ---
    get:
        description: Get List of Todos
        responses:
            200:
                description: Return a todo list
                content:
                    application/json:
                        schema: TodoListResponseSchema
    """

    return services.todo()
