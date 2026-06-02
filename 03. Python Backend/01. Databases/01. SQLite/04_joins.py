# 04 — JOIN (two related tables)
# Run: python 04_joins.py

import sqlite3
import os

conn = sqlite3.connect("join_demo.db")
cur = conn.cursor()

cur.execute("CREATE TABLE dept (id INT PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE emp (id INT PRIMARY KEY, name TEXT, dept_id INT)")
cur.executemany("INSERT INTO dept VALUES (?,?)", [(1, "IT"), (2, "HR")])
cur.executemany("INSERT INTO emp VALUES (?,?,?)", [(1, "Asha", 1), (2, "Ravi", 2), (3, "Meera", 1)])
conn.commit()

cur.execute("""
SELECT e.name, d.name AS department
FROM emp e
INNER JOIN dept d ON e.dept_id = d.id
""")
for row in cur.fetchall():
    print(row)

conn.close()
os.remove("join_demo.db")
