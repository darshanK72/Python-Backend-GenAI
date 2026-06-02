# 02 — SQL CRUD with SQLite
# Run: python 02_sql_crud.py

import sqlite3
import os

DB = "crud_demo.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
)
""")

# CREATE (insert)
cur.executemany(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    [("Pen", 20), ("Notebook", 120)],
)

# READ
cur.execute("SELECT * FROM products WHERE price > ?", (50,))
print("expensive:", cur.fetchall())

# UPDATE
cur.execute("UPDATE products SET price = ? WHERE name = ?", (25, "Pen"))

# DELETE
cur.execute("DELETE FROM products WHERE name = ?", ("Notebook",))

conn.commit()
cur.execute("SELECT * FROM products")
print("final:", cur.fetchall())

conn.close()
os.remove(DB)
