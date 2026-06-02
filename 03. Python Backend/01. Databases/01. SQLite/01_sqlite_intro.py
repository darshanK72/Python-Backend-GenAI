# 01 — SQLite (no server required)
# Run: python 01_sqlite_intro.py
#
# SQLite is a file-based database built into Python.
# Practice SQL here before MySQL.

import sqlite3
import os

DB_PATH = "demo_learning.db"

# --- 1. Connect (creates file if missing) ---
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
print("Connected to", os.path.abspath(DB_PATH))

# --- 2. Create table ---
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER
)
""")

# --- 3. Insert ---
cur.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Asha", 88))
cur.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Ravi", 76))
conn.commit()

# --- 4. Select ---
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

conn.close()
os.remove(DB_PATH)
print("Cleanup: removed", DB_PATH)
