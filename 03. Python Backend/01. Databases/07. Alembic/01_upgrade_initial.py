# 01 — Apply initial migration (upgrade to 001_initial)
# Run: python 01_upgrade_initial.py

import os
from pathlib import Path

from alembic import command
from alembic.config import Config

BASE = Path(__file__).resolve().parent
DB_FILE = BASE / "shop_alembic.db"

if DB_FILE.exists():
    os.remove(DB_FILE)

cfg = Config(str(BASE / "alembic.ini"))
command.upgrade(cfg, "001_initial")
print("Upgraded to 001_initial")
print("Database:", DB_FILE)
