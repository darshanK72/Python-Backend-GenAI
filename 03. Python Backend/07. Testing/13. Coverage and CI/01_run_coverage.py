# 01 — Generate coverage report
# Run: pytest --cov=notes_service --cov-report=term-missing 01_run_coverage.py -v
#       (from folder 03. Unit Testing Services, or adjust path below)

import subprocess
import sys
from pathlib import Path

SERVICE = Path(__file__).resolve().parents[1] / "03. Unit Testing Services"


def main():
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "01_test_notes_service.py",
        "--cov=notes_service",
        "--cov-report=term-missing",
        "-v",
    ]
    print("Running from:", SERVICE, "\n")
    raise SystemExit(subprocess.call(cmd, cwd=SERVICE))


if __name__ == "__main__":
    main()
