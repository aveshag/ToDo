from flask import Flask, render_template

import grpc
import todo_pb2_grpc
import todo_pb2


app = Flask(__name__)
channel = grpc.insecure_channel("localhost:40000")
client = todo_pb2_grpc.TodoStub(channel)


@app.route("/todo/<text>")
def add_todo(text):
    todo_text = todo_pb2.TodoText(text=text)
    todo = client.createTodo(todo_text)
    return todo.id


@app.route("/")
def get_all_todos():
    todos = client.readTodos(todo_pb2.noParam())
    return render_template(
        "homepage.html",
        todo_items=todos.items
    )
