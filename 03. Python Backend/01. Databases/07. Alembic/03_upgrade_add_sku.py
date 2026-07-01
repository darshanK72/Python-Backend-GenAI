# 03 — Apply second migration (add sku column)
# Run: python 03_upgrade_add_sku.py
# Prerequisite: 01 and 02

from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Product

BASE = Path(__file__).resolve().parent
cfg = Config(str(BASE / "alembic.ini"))

command.upgrade(cfg, "002_add_sku")
print("Upgraded to 002_add_sku")

engine = create_engine(f"sqlite:///{BASE / 'shop_alembic.db'}")
with Session(engine) as session:
    for product in session.scalars(select(Product)):
        product.sku = f"SKU-{product.id:03d}"
    session.commit()

    for p in session.scalars(select(Product).order_by(Product.id)):
        print(p.id, p.name, p.sku)
