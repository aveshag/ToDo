import grpc
import logging
import todo_pb2_grpc
import todo_pb2


def add_todo(stub, text):
    todo_text = todo_pb2.TodoText(text=text)
    todo_item = stub.createTodo(todo_text)
    return todo_item


def get_all_todos(stub):
    return stub.readTodos(todo_pb2.noParam())


def run():
    with grpc.insecure_channel("localhost:40000") as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        print("Creating todo1: \n")
        print(add_todo(stub, "Cooking"))
        print("Creating todo2: \n")
        print(add_todo(stub, "Cycling"))
        print("All todos created: \n")
        print(get_all_todos(stub))


if __name__ == "__main__":
    logging.basicConfig()
    run()
