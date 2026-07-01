# 02 — Run the full capstone suite
# Run: python 02_run_capstone.py

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    cmd = [sys.executable, "-m", "pytest", str(HERE / "test_notes_api.py"), "-v"]
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
