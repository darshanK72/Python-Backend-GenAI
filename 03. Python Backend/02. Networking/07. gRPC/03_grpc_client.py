# 03 — gRPC client
# Run: python 03_grpc_client.py  (start 02_grpc_server.py first)

import sys
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

TARGET = "127.0.0.1:50051"

if __name__ == "__main__":
    with grpc.insecure_channel(TARGET) as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeter_pb2.HelloRequest(name="Learner"))
        print("Reply:", response.message)
