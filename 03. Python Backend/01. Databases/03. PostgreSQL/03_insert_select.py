# 03 — INSERT and SELECT
# Run: python 03_insert_select.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import POSTGRES

import psycopg

if __name__ == "__main__":
    conn = psycopg.connect(
        host=POSTGRES["host"],
        port=POSTGRES["port"],
        user=POSTGRES["user"],
        password=POSTGRES["password"],
        dbname=POSTGRES["database"],
    )
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO student (roll_no, name, marks, city)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (roll_no) DO NOTHING
                """,
                (101, "Darshan", 88, "Nashik"),
            )
            cur.execute(
                """
                INSERT INTO student (roll_no, name, marks, city)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (roll_no) DO NOTHING
                """,
                (102, "Asha", 92, "Pune"),
            )
            cur.execute("SELECT roll_no, name, marks, city FROM student ORDER BY roll_no")
            for row in cur.fetchall():
                print(row)
        conn.commit()
    finally:
        conn.close()
