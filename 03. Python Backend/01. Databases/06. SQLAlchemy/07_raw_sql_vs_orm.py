# 07 — Raw SQL vs ORM (same task, two styles)
# Run: python 07_raw_sql_vs_orm.py

import os
from pathlib import Path

from sqlalchemy import Integer, String, create_engine, select, text
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DB_PATH = Path(__file__).with_name("compare_demo.db")
if DB_PATH.exists():
    os.remove(DB_PATH)


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80))


engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([Item(name="alpha"), Item(name="beta")])
    session.commit()

print("--- Raw SQL ---")
with engine.connect() as conn:
    for row in conn.execute(text("SELECT id, name FROM items WHERE name LIKE 'a%'")):
        print(row)

print("--- ORM ---")
with Session(engine) as session:
    for item in session.scalars(select(Item).where(Item.name.like("a%"))):
        print(item.id, item.name)

engine.dispose()
if DB_PATH.exists():
    os.remove(DB_PATH)
