# 02 — Audit dependencies with pip-audit
# Run: python 02_pip_audit.py
# Install: pip install pip-audit

import subprocess
import sys
from pathlib import Path

REQ = Path(__file__).resolve().parents[3] / "requirements.txt"


def run_pip_audit() -> int:
    cmd = [sys.executable, "-m", "pip_audit"]
    if REQ.exists():
        cmd.extend(["-r", str(REQ)])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout or result.stderr)
        return result.returncode
    except Exception:
        print("Install: pip install pip-audit")
        return 1


if __name__ == "__main__":
    print("Checking known vulnerabilities in installed packages...\n")
    run_pip_audit()
