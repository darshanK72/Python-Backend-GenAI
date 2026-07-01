# 01 — Build and run a Docker image
# Run: python 01_build_and_run.py
# Requires Docker Desktop installed

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = "backend-lesson-api:latest"


def run(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    return subprocess.call(cmd, cwd=HERE)


if __name__ == "__main__":
    print("Docker workflow for this folder:\n")
    steps = [
        ["docker", "build", "-t", IMAGE, "."],
        ["docker", "run", "--rm", "-p", "8000:8000", IMAGE],
    ]
    for cmd in steps:
        print(" ", " ".join(cmd))
    print("\nThen open: http://127.0.0.1:8000/health")
    if len(sys.argv) > 1 and sys.argv[1] == "--build":
        raise SystemExit(run(steps[0]))
