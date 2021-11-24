from typing import Any

from app.schemas.todo import TodoListResponseSchema


def todo() -> Any:
    dummy_data = [
        {"id": 1, "title": "Finish this task", "status": False},
        {"id": 2, "title": "Finish that task", "status": True},
    ]

    return TodoListResponseSchema().dump({"todo_list": dummy_data})
