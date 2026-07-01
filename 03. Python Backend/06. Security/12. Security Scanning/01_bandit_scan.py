# 01 — Run Bandit static security scan
# Run: python 01_bandit_scan.py
# Install: pip install bandit

import subprocess
import sys
from pathlib import Path

TARGET = Path(__file__).resolve().parent.parent / "06. Web Vulnerabilities" / "01_sql_injection.py"


def run_bandit(path: Path) -> int:
    try:
        result = subprocess.run(
            [sys.executable, "-m", "bandit", "-q", str(path)],
            capture_output=True,
            text=True,
        )
        print(result.stdout or result.stderr or "(no output)")
        return result.returncode
    except FileNotFoundError:
        print("Install: pip install bandit")
        return 1


if __name__ == "__main__":
    print(f"Scanning: {TARGET.name}\n")
    code = run_bandit(TARGET)
    print("\nBandit flags risky patterns (hardcoded passwords, unsafe SQL, etc.).")
