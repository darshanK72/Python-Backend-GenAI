# 06 — Transactions (commit / rollback)
# Run: python 06_transactions.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL
import pymysql

conn = pymysql.connect(**MYSQL)
try:
    conn.begin()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO student (roll_no, name, marks, city) VALUES (%s,%s,%s,%s)",
            (201, "Test User", 70, "Mumbai"),
        )
    # conn.rollback()   # uncomment to cancel insert
    conn.commit()
    print("Transaction committed")
except pymysql.Error as e:
    conn.rollback()
    print("Rolled back:", e)
finally:
    conn.close()
