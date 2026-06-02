# 05 — Database helper class (reusable pattern)
# Run: python 05_dbhelper_class.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL
import pymysql


class DbHelper:
    def __init__(self):
        self.conn = pymysql.connect(**MYSQL)

    def execute(self, query, params=None):
        with self.conn.cursor() as cur:
            cur.execute(query, params or ())
        self.conn.commit()

    def fetch_all(self, query, params=None):
        with self.conn.cursor() as cur:
            cur.execute(query, params or ())
            return cur.fetchall()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = DbHelper()
    try:
        rows = db.fetch_all("SELECT * FROM student")
        for row in rows:
            print(row)
    finally:
        db.close()
