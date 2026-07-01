# 02 — gRPC server
# Run: python 01_generate_stubs.py  (once)
#       python 02_grpc_server.py
# Then: python 03_grpc_client.py

import sys
from concurrent import futures
from pathlib import Path

try:
    import grpc
except ImportError:
    print("Install: pip install grpcio grpcio-tools")
    raise SystemExit(1)

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))


def ensure_generated():
    if (BASE / "greeter_pb2.py").exists() and (BASE / "greeter_pb2_grpc.py").exists():
        return
    import subprocess

    subprocess.check_call([sys.executable, str(BASE / "01_generate_stubs.py")])


ensure_generated()

try:
    import greeter_pb2
    import greeter_pb2_grpc
except ImportError:
    print("Run: python 01_generate_stubs.py first")
    raise SystemExit(1)

HOST = "127.0.0.1"
PORT = 50051


class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message=f"Hello, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(f"{HOST}:{PORT}")
    server.start()
    print(f"gRPC server on {HOST}:{PORT}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
