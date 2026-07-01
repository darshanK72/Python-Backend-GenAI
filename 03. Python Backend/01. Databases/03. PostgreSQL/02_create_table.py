# 02 — CREATE TABLE
# Run: python 02_create_table.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import POSTGRES

import psycopg

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS student (
    roll_no INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    marks INTEGER,
    city VARCHAR(50)
)
"""

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
            cur.execute(CREATE_SQL)
        conn.commit()
        print("Table student ready")
    finally:
        conn.close()
