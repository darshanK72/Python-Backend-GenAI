# 02 — ORM CRUD after migration
# Run: python 02_orm_crud.py
# Prerequisite: python 01_upgrade_initial.py

from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Product

BASE = Path(__file__).resolve().parent
engine = create_engine(f"sqlite:///{BASE / 'shop_alembic.db'}")

with Session(engine) as session:
    session.add_all([Product(name="Pen"), Product(name="Notebook")])
    session.commit()

    rows = session.scalars(select(Product).order_by(Product.id)).all()
    for p in rows:
        print(p.id, p.name)
