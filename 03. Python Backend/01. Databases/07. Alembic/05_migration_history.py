# 05 — Migration history and current revision
# Run: python 05_migration_history.py

from pathlib import Path

from alembic import command
from alembic.config import Config

BASE = Path(__file__).resolve().parent
cfg = Config(str(BASE / "alembic.ini"))

print("Current revision:")
command.current(cfg, verbose=True)

print("\nHistory:")
command.history(cfg, verbose=True)
