# 01 — Safe filenames (prevent path traversal)
# Run: python 01_safe_filenames.py

import re
from pathlib import Path

UPLOAD_ROOT = Path(__file__).resolve().parent / "_uploads"
ALLOWED = re.compile(r"^[a-zA-Z0-9._-]+$")


def safe_filename(name: str) -> str | None:
    base = Path(name).name
    if not base or not ALLOWED.match(base):
        return None
    if base in {".", ".."}:
        return None
    return base


def resolve_upload_path(name: str) -> Path | None:
    safe = safe_filename(name)
    if not safe:
        return None
    target = (UPLOAD_ROOT / safe).resolve()
    if UPLOAD_ROOT.resolve() not in target.parents and target != UPLOAD_ROOT.resolve():
        return None
    return target


if __name__ == "__main__":
    UPLOAD_ROOT.mkdir(exist_ok=True)
    for attempt in ["report.pdf", "../../etc/passwd", "bad name.exe"]:
        print(attempt, "->", resolve_upload_path(attempt))
