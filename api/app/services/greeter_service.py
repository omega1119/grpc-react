from app.protos import example_pb2, example_pb2_grpc

class GreeterService(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return example_pb2.HelloReply(message=f"Hello, {request.name}!")
