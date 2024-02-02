import json
import os

DB_FILE = "db.json"


def write_todo(todo_item):
    todos = []
    if os.path.isfile(DB_FILE):
        with open(DB_FILE, mode='r') as f:
            todos = json.load(f)
    todos.append(todo_item)
    with open(DB_FILE, mode="w") as f:
        json.dump(todos, f, indent=2)


def read_todos():
    if not os.path.isfile(DB_FILE):
        return None
    with open(DB_FILE, "r") as f:
        return json.load(f)
