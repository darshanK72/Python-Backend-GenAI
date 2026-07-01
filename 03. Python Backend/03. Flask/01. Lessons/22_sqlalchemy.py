# 22 — SQLAlchemy ORM
# Run: python 22_sqlalchemy.py
# Uses books_demo.db in this folder.

import os

from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

DB_PATH = os.path.join(os.path.dirname(__file__), "books_demo.db")
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class BookRow(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)

app = Flask(__name__)


@app.get("/books")
def list_books():
    db = SessionLocal()
    try:
        rows = db.query(BookRow).all()
        return jsonify([{"id": r.id, "title": r.title, "author": r.author} for r in rows])
    finally:
        db.close()


@app.post("/books")
def create_book():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    author = str(data.get("author", "")).strip()
    if not title or not author:
        return jsonify({"error": "title and author required"}), 400
    db = SessionLocal()
    try:
        row = BookRow(title=title, author=author)
        db.add(row)
        db.commit()
        db.refresh(row)
        return jsonify({"id": row.id, "title": row.title, "author": row.author}), 201
    finally:
        db.close()


@app.get("/books/<int:book_id>")
def get_book(book_id: int):
    db = SessionLocal()
    try:
        row = db.get(BookRow, book_id)
        if not row:
            return jsonify({"error": "Not found"}), 404
        return jsonify({"id": row.id, "title": row.title, "author": row.author})
    finally:
        db.close()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
