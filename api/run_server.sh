#!/bin/bash

cd "$(dirname "$0")"  # makes sure we're in the api/ dir

echo "Generating gRPC code..."
python -m grpc_tools.protoc \
  -I./app/protos \
  --python_out=./app \
  --grpc_python_out=./app \
  ./app/protos/example.proto

echo "Starting gRPC server..."
python -m app.server
