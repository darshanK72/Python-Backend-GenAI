# 04 — UPDATE and DELETE
# Run: python 04_update_delete.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL
import pymysql

conn = pymysql.connect(**MYSQL)
try:
    with conn.cursor() as cur:
        cur.execute("UPDATE student SET marks = %s WHERE roll_no = %s", (90, 101))
        cur.execute("DELETE FROM student WHERE roll_no = %s", (102,))
    conn.commit()
    print("Updated and deleted")

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM student")
        print(cur.fetchall())
finally:
    conn.close()
