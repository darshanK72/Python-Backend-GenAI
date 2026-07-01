# 03 — Dependency pinning reminder
# Run: python 03_dependency_pinning.py

from pathlib import Path

REQ = Path(__file__).resolve().parents[3] / "requirements.txt"

if __name__ == "__main__":
    print("Pin versions in requirements.txt for reproducible builds.")
    print("Review updates regularly; run pip-audit after upgrades.\n")
    if REQ.exists():
        lines = [ln for ln in REQ.read_text(encoding="utf-8").splitlines() if ln and not ln.startswith("#")]
        print(f"Root requirements.txt has {len(lines)} pinned packages.")
    print("\nGood:  requests>=2.31")
    print("Better: requests==2.31.0  (exact pin in production lock files)")
