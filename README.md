# grpc-react

A full-stack project using gRPC for the backend and React (Next.js + TypeScript) for the frontend. This setup allows communication between a Python gRPC server and a browser-based client using gRPC-Web through Envoy as a proxy.

---

## 🧱 Prerequisites

- Conda: https://docs.conda.io/en/latest/
- Homebrew: https://brew.sh/
- Docker: https://www.docker.com/
- Node.js & npm: https://nodejs.org/
- nvm: https://github.com/nvm-sh/nvm
- Python 3.9

---

## 🐍 Python Environment Setup

```bash
conda create -n grpc_env python=3.9 -y
conda activate grpc_env

python -m pip install grpcio grpcio-tools
```

---

## 🔧 Install gRPC Tools

```bash
brew install grpc
brew install grpcurl
```

---

## 🛸️ Compile gRPC Protos (Python)

```bash
# Make the server script executable
chmod +x api/run_server.sh

# Generate gRPC Python code from .proto file
python -m grpc_tools.protoc -I. \
  --python_out=. \
  --grpc_python_out=. \
  app/protos/example.proto

# (Optional) Remove generated Python files if regenerating
rm app/protos/example_pb2*.py
```

---

## 🚀 Run the gRPC Python Client

```bash
python client_script/test_client.py
```

---

## 🟢 Node + gRPC-Web Setup

### Install & Configure `nvm`

```bash
brew install nvm

# Add to ~/.zshrc
nano ~/.zshrc
# Add:
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Optionally add bash completion to ~/.bash_profile
nano ~/.bash_profile
# Add:
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

### Use Node v20

```bash
nvm use 20
```

### Install gRPC-Web Tooling

```bash
npm install -g protoc-gen-js protoc-gen-grpc-web
```

---

## ⚛️ Create React Frontend with TypeScript

```bash
cd client
npx create-next-app@latest . --typescript
```

---

## 📦 Install gRPC-Web Frontend Dependencies

```bash
cd client

npm install grpc-web
npm install google-protobuf
npm install @improbable-eng/grpc-web
```

---

## 📡 Run Envoy Proxy

Make sure you have `envoy.yaml` configured correctly.

```bash
docker run -d --name envoy \
  -p 8080:8080 \
  -p 9901:9901 \
  -v "$PWD/envoy.yaml":/etc/envoy/envoy.yaml \
  envoyproxy/envoy:v1.29-latest
```

---

## 📁 Compile Protos for gRPC-Web (Frontend)

```bash
protoc -I=./api/app/protos \
  ./api/app/protos/example.proto \
  --js_out=import_style=commonjs:./client/proto \
  --grpc-web_out=import_style=typescript,mode=grpcwebtext:./client/proto
```

---

## 📌 Notes

- Make sure `envoy.yaml` routes correctly between your gRPC server and the web client.
- Your frontend app should use the generated TypeScript files in `client/proto` to communicate via gRPC-Web.
- You may need to expose your Python gRPC server on the correct port expected by Envoy (usually 50051).

---

## 🧚 To Do

- [ ] Add working server and client example
- [ ] Add unit tests
- [ ] Document how to run the full-stack setup (dev vs prod)

