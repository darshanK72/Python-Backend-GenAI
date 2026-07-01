# 06 — Third migration + ORM insert
# Run: python 06_apply_categories_migration.py
# Prerequisite: run 01 -> 03 first (or start fresh with 01)

from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Category

BASE = Path(__file__).resolve().parent
cfg = Config(str(BASE / "alembic.ini"))

command.upgrade(cfg, "003_add_categories")
print("Upgraded to 003_add_categories")

engine = create_engine(f"sqlite:///{BASE / 'shop_alembic.db'}")
with Session(engine) as session:
    session.add_all([Category(name="Stationery"), Category(name="Electronics")])
    session.commit()
    for cat in session.scalars(select(Category).order_by(Category.id)):
        print(cat.id, cat.name)
