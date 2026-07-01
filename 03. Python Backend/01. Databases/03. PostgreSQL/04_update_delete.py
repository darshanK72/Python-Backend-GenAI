# 04 — UPDATE and DELETE
# Run: python 04_update_delete.py

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
                "UPDATE student SET marks = %s WHERE roll_no = %s",
                (95, 101),
            )
            print("Updated rows:", cur.rowcount)

            cur.execute("DELETE FROM student WHERE roll_no = %s", (102,))
            print("Deleted rows:", cur.rowcount)

            cur.execute("SELECT * FROM student ORDER BY roll_no")
            print("Remaining:", cur.fetchall())
        conn.commit()
    finally:
        conn.close()
