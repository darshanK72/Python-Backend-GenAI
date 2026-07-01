# 06 — Transactions (commit / rollback)
# Run: python 06_transactions.py

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
        with conn.transaction():
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO student (roll_no, name, marks, city)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (roll_no) DO UPDATE
                    SET marks = EXCLUDED.marks
                    """,
                    (201, "Txn User", 77, "Mumbai"),
                )
        print("Transaction committed")
        # To test rollback, wrap in try/except and call conn.rollback()
    except psycopg.Error as e:
        print("Transaction failed:", e)
    finally:
        conn.close()
