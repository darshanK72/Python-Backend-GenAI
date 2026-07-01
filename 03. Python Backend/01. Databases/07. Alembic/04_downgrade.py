# 04 — Downgrade one revision
# Run: python 04_downgrade.py
# Rolls back 002_add_sku -> 001_initial

from pathlib import Path

from alembic import command
from alembic.config import Config

BASE = Path(__file__).resolve().parent
cfg = Config(str(BASE / "alembic.ini"))

command.downgrade(cfg, "-1")
print("Downgraded one revision")
command.current(cfg)
