# 01 — Generate gRPC Python stubs from greeter.proto
# Run: python 01_generate_stubs.py
# Install: pip install grpcio grpcio-tools

import sys
from pathlib import Path

try:
    from grpc_tools import protoc
except ImportError:
    print("Install: pip install grpcio grpcio-tools")
    raise SystemExit(1)

BASE = Path(__file__).resolve().parent
proto = BASE / "greeter.proto"

result = protoc.main(
    [
        "grpc_tools.protoc",
        f"-I{BASE}",
        f"--python_out={BASE}",
        f"--grpc_python_out={BASE}",
        str(proto),
    ]
)
if result != 0:
    raise SystemExit(f"protoc failed with code {result}")

print("Generated: greeter_pb2.py, greeter_pb2_grpc.py")
