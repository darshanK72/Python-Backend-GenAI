# 04 — Relationships (one-to-many)
# Run: python 04_relationships.py

import os
from pathlib import Path

from sqlalchemy import ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DB_PATH = Path(__file__).with_name("relations_demo.db")
if DB_PATH.exists():
    os.remove(DB_PATH)


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "departments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    employees: Mapped[list["Employee"]] = relationship(back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))
    department: Mapped[Department] = relationship(back_populates="employees")


engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(engine)

with Session(engine) as session:
    it = Department(name="IT")
    it.employees = [Employee(name="Asha"), Employee(name="Meera")]
    session.add(it)
    session.commit()

    for emp in session.scalars(select(Employee)).all():
        print(emp.name, "->", emp.department.name)

engine.dispose()
if DB_PATH.exists():
    os.remove(DB_PATH)
