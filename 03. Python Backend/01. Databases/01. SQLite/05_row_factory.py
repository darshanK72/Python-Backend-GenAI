# 05 — Row as dict (sqlite3.Row)
# Run: python 05_row_factory.py

import sqlite3
import os

conn = sqlite3.connect("row_demo.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("CREATE TABLE users (id INT, email TEXT)")
cur.execute("INSERT INTO users VALUES (1, 'a@example.com')")
conn.commit()

cur.execute("SELECT * FROM users")
row = cur.fetchone()
print("as dict:", dict(row))
print("email:", row["email"])

conn.close()
os.remove("row_demo.db")
