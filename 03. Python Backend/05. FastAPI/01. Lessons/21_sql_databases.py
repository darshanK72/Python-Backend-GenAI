# 21 — SQL databases (SQLAlchemy + SQLite)
# Run: uvicorn 21_sql_databases:app --reload --port 8000
# Uses a local SQLite file; safe to delete books_demo.db after practice.

import os

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

DB_PATH = os.path.join(os.path.dirname(__file__), "books_demo.db")
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class BookRow(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lesson 21 — SQL Databases")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books", response_model=list[Book])
def list_books(db: Session = Depends(get_db)):
    rows = db.query(BookRow).all()
    return [Book(id=r.id, title=r.title, author=r.author) for r in rows]


@app.post("/books", response_model=Book, status_code=201)
def create_book(payload: BookCreate, db: Session = Depends(get_db)):
    row = BookRow(title=payload.title, author=payload.author)
    db.add(row)
    db.commit()
    db.refresh(row)
    return Book(id=row.id, title=row.title, author=row.author)


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    row = db.get(BookRow, book_id)
    if not row:
        raise HTTPException(404, "Book not found")
    return Book(id=row.id, title=row.title, author=row.author)
