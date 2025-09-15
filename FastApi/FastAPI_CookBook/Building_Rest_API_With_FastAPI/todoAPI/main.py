from fastapi import FastAPI, HTTPException
from model import (
    Todo,
    TodoWithID,
)
from operations import read_all_todos, create_todo, update_todo, delete_todo
from pydantic import BaseModel


class UpdateTodo(BaseModel):
    todos_title: str | None = None
    todos_completed: bool | None = None
    todos_userId: int | None = None


app = FastAPI()


@app.get("/todos", response_model=list[TodoWithID])
def get_todos():
    todos = read_all_todos()
    return todos


@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    todo = read_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo


@app.post("/todo", response_model=TodoWithID)
def add_todo(todo: Todo):
    return create_todo(todo)


@app.put("/todo/{todo_id}", response_model=TodoWithID)
def update_todo(todo_id: int, todo_update: UpdateTodo):
    modified = modify_todo(
        todo_id,
        todo_update.model_dump(exclude_unset=True),
    )
    if not modified:
        raise HTTPException(status_code=404, detail="todo not found")
    return modified


@app.delete("/todo/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    removed_todo = remove_todo(todo_id)
    if not removed_todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return removed_todo
