# 03 — INSERT and SELECT
# Run: python 03_insert_select.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL
import pymysql

conn = pymysql.connect(**MYSQL)
try:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO student (roll_no, name, marks, city) VALUES (%s, %s, %s, %s)",
            (101, "Darshan", 88, "Nashik"),
        )
        cur.execute(
            "INSERT INTO student (roll_no, name, marks, city) VALUES (%s, %s, %s, %s)",
            (102, "Asha", 92, "Pune"),
        )
    conn.commit()

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        for row in rows:
            print(row)
finally:
    conn.close()
