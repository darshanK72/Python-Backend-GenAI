# 04 — sqlite3 (built-in database)
# Run: python 04_sqlite3.py

import sqlite3
import os

db_path = "demo_library.db"

# --- 1. Connect and create table ---
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    year INTEGER
)
""")

# --- 2. Insert ---
cur.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            ("Python Basics", "Darshan", 2026))
cur.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            ("Data Science 101", "Asha", 2025))
conn.commit()

# --- 3. Query ---
cur.execute("SELECT id, title, author FROM books ORDER BY year DESC")
for row in cur.fetchall():
    print(row)

# --- 4. Parameterized query (safe) ---
cur.execute("SELECT title FROM books WHERE author = ?", ("Darshan",))
print("Darshan's books:", cur.fetchall())

conn.close()
os.remove(db_path)
print("DB removed:", db_path)
