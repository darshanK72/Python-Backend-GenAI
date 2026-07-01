# 05 — Filtering, ordering, aggregates
# Run: python 05_query_filtering.py

import os
from pathlib import Path

from sqlalchemy import Integer, String, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DB_PATH = Path(__file__).with_name("query_demo.db")
if DB_PATH.exists():
    os.remove(DB_PATH)


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    marks: Mapped[int] = mapped_column(Integer)
    city: Mapped[str] = mapped_column(String(50))


engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all(
        [
            Student(name="Asha", marks=88, city="Pune"),
            Student(name="Ravi", marks=76, city="Nashik"),
            Student(name="Meera", marks=92, city="Pune"),
        ]
    )
    session.commit()

    top = session.scalars(select(Student).where(Student.marks >= 85).order_by(Student.marks.desc()))
    print("Top students:")
    for s in top:
        print(s.name, s.marks)

    avg_marks = session.scalar(select(func.avg(Student.marks)))
    print("Average marks:", round(avg_marks, 2))

engine.dispose()
if DB_PATH.exists():
    os.remove(DB_PATH)
