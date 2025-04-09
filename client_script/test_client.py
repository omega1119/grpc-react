import sys
import os

# Add the api/ folder to sys.path BEFORE importing anything from app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api')))

import grpc
from app.protos import example_pb2, example_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = example_pb2_grpc.GreeterStub(channel)

    name = "Simon"
    request = example_pb2.HelloRequest(name=name)
    response = stub.SayHello(request)

    print("Client received:", response.message)

if __name__ == '__main__':
    run()
