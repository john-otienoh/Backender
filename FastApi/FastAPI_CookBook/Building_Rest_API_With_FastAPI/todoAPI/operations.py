import csv
from typing import Optional
from model import Todo, TodoWithID

DATABASE_FILENAME = "todos.csv"
column_fields = ["todos_id", "todos_title", "todos_completed", "todos_userId"]


def read_all_todos() -> list[TodoWithID]:
    with open(DATABASE_FILENAME, encoding="uft-8") as csvfile:
        reader = csv.DictReader(
            csvfile,
        )
        return [TodoWithID(**row) for row in reader]


def read_todo(todo_id) -> Optional[TodoWithID]:
    with open(DATABASE_FILENAME, encoding="utf-8") as csvfile:
        reader = csv.DictReader(
            csvfile,
        )
        for row in reader:
            if int(row["todos_id"]) == todo_id:
                return TodoWithID(**row)


def get_next_id():
    try:
        with open(DATABASE_FILENAME, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            max_id = max(int(row["todos_id"]) for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1


def write_todo_into_csv(todo: TodoWithID):
    with open(DATABASE_FILENAME, mode="a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=column_fields,
        )
        writer.writerow(todo.model_dump())


def create_todo(todo: Todo) -> TodoWithID:
    id = get_next_id()
    todo_with_id = TodoWithID(id=id, **todo.model_dump())
    write_todo_into_csv(todo_with_id)
    return todo_with_id


def update_todo(id: int, todo: dict) -> Optional[TodoWithID]:
    updated_todo: Optional[TodoWithID] = None
    todos = read_all_todos()
    for number, todo_ in enumerate(todos):
        if todo_.id == id:
            todos[number] = updated_todo = todo_.model_copy(update=todo)
    with open(DATABASE_FILENAME, mode="w", newline="") as csvfile:  # rewrite the file
        writer = csv.DictWriter(
            csvfile,
            fieldnames=column_fields,
        )
        writer.writeheader()
        for todo in todos:
            writer.writerow(todo.model_dump())
    if updated_todo:
        return updated_todo


def delete_todo(id: int) -> bool:
    deleted_todo: Optional[Todo] = None
    todos = read_all_todos()
    with open(DATABASE_FILENAME, mode="w", newline="") as csvfile:  # rewrite the file
        writer = csv.DictWriter(
            csvfile,
            fieldnames=column_fields,
        )
        writer.writeheader()
        for todo in todos:
            if todo.id == id:
                deleted_todo = todo
                continue
            writer.writerow(todo.model_dump())
    if deleted_todo:
        dict_todo_without_id = deleted_todo.model_dump()
        del dict_todo_without_id["id"]
        return Todo(**dict_todo_wihtout_id)
