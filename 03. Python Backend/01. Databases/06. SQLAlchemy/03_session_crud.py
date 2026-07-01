# 03 — Session CRUD
# Run: python 03_session_crud.py

import os
from pathlib import Path

from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DB_PATH = Path(__file__).with_name("session_demo.db")
if DB_PATH.exists():
    os.remove(DB_PATH)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)


engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([Product(name="Pen", price=20), Product(name="Notebook", price=120)])
    session.commit()

    products = session.scalars(select(Product).where(Product.price >= 50)).all()
    for p in products:
        print(p.id, p.name, p.price)

    notebook = session.scalar(select(Product).where(Product.name == "Notebook"))
    notebook.price = 99
    session.commit()
    print("Updated:", notebook.name, notebook.price)

engine.dispose()
if DB_PATH.exists():
    os.remove(DB_PATH)
