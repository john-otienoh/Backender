from pydantic import BaseModel


class Todo(BaseModel):
    todos_title: str
    todos_completed: bool
    todos_userId: int


class TodoWithID(Todo):
    todos_id: int
