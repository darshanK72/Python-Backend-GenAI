# 06 — SQLAlchemy with MySQL engine
# Run: python 06_mysql_engine.py
# Requires MySQL + .env (same as 02. MySQL lessons)

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL

from sqlalchemy import create_engine, text

url = (
    f"mysql+pymysql://{MYSQL['user']}:{MYSQL['password']}"
    f"@{MYSQL['host']}:{MYSQL['port']}/{MYSQL['database']}?charset=utf8mb4"
)
engine = create_engine(url, echo=False)

with engine.connect() as conn:
    rows = conn.execute(text("SELECT roll_no, name, marks, city FROM student LIMIT 5")).fetchall()
    if not rows:
        print("No rows — run MySQL 03_insert_select.py first")
    for row in rows:
        print(row)

print("MySQL engine OK")
