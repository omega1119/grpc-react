import grpc
from concurrent import futures
from app.protos import example_pb2_grpc
from app.services.greeter_service import GreeterService
from app.config import settings

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port(f"[::]:{settings['PORT']}")
    print(f"Server starting on port {settings['PORT']}...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
