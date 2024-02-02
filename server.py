from concurrent import futures

import grpc
import dao
import util
import logging
import todo_pb2_grpc
import todo_pb2


class TodoServicer(todo_pb2_grpc.TodoServicer):
    def createTodo(self, request, context):
        text = request.text
        todo_item = {"id": util.get_uuid(), "text": text}
        dao.write_todo(todo_item)
        return todo_pb2.TodoItem(**todo_item)

    def readTodos(self, request, context):
        items = dao.read_todos()
        return todo_pb2.TodoItems(items=items)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(
        TodoServicer(), server
    )
    server.add_insecure_port("[::]:40000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
