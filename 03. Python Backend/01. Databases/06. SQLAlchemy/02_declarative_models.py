# 02 — Declarative models
# Run: python 02_declarative_models.py

import os
from pathlib import Path

from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DB_PATH = Path(__file__).with_name("models_demo.db")
if DB_PATH.exists():
    os.remove(DB_PATH)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    author_id: Mapped[int] = mapped_column(Integer)


engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(engine)
print("Tables:", list(Base.metadata.tables.keys()))
engine.dispose()
if DB_PATH.exists():
    os.remove(DB_PATH)
