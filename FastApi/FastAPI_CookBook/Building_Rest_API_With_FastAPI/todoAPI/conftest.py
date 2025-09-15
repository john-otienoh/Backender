TEST_DATABASE_FILE = "test_todos.csv"
TEST_TODOS_CSV = [
    {
        "id": "1",
        "title": "Test TODO One",
        "description": "Test Description One",
        "status": "Incomplete",
    },
    {
        "id": "2",
        "title": "Test TODO Two",
        "description": "Test Description Two",
        "status": "Ongoing",
    },
]
TEST_TODOS = [{**todo_json, "id": int(todo_json["id"])} for todo_json in TEST_TODOS_CSV]
