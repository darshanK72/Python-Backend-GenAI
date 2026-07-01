# 01 — Engine and text() queries (SQLAlchemy Core)
# Run: python 01_engine_and_text.py
# Uses local SQLite — no server required.

import os
from pathlib import Path

from sqlalchemy import create_engine, text

DB_PATH = Path(__file__).with_name("core_demo.db")
if DB_PATH.exists():
    os.remove(DB_PATH)

engine = create_engine(f"sqlite:///{DB_PATH}")

with engine.begin() as conn:
    conn.execute(
        text(
            """
            CREATE TABLE book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL
            )
            """
        )
    )
    conn.execute(text("INSERT INTO book (title) VALUES (:t)"), [{"t": "Clean Code"}, {"t": "Fluent Python"}])

with engine.connect() as conn:
    rows = conn.execute(text("SELECT id, title FROM book ORDER BY id")).fetchall()
    for row in rows:
        print(row)

engine.dispose()
if DB_PATH.exists():
    os.remove(DB_PATH)
print("Done")
