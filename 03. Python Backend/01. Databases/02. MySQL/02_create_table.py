# 02 — CREATE TABLE
# Run: python 02_create_table.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL
import pymysql

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    marks INT,
    city VARCHAR(50)
)
"""

conn = pymysql.connect(**MYSQL)
try:
    with conn.cursor() as cur:
        cur.execute(CREATE_SQL)
    conn.commit()
    print("Table student ready")
finally:
    conn.close()
