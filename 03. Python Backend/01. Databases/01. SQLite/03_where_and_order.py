# 03 — WHERE, ORDER BY, LIMIT
# Run: python 03_where_and_order.py

import sqlite3
import os

conn = sqlite3.connect("query_demo.db")
cur = conn.cursor()
cur.execute("CREATE TABLE scores (name TEXT, subject TEXT, marks INT)")
data = [
    ("Asha", "Math", 90),
    ("Asha", "Science", 85),
    ("Ravi", "Math", 76),
    ("Ravi", "Science", 92),
]
cur.executemany("INSERT INTO scores VALUES (?,?,?)", data)
conn.commit()

cur.execute(
    "SELECT name, marks FROM scores WHERE subject = ? ORDER BY marks DESC LIMIT 2",
    ("Math",),
)
print("top Math:", cur.fetchall())

conn.close()
os.remove("query_demo.db")
