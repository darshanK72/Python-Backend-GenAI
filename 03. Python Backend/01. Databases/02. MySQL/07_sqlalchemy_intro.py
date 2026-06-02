# 07 — SQLAlchemy intro (ORM — optional, uncomment in requirements.txt)
# Run: python 07_sqlalchemy_intro.py
#
# pip install sqlalchemy

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL

try:
    from sqlalchemy import create_engine, text
except ImportError:
    print("Install: pip install sqlalchemy")
    raise SystemExit(1)

url = (
    f"mysql+pymysql://{MYSQL['user']}:{MYSQL['password']}"
    f"@{MYSQL['host']}:{MYSQL['port']}/{MYSQL['database']}"
)
engine = create_engine(url, echo=False)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM student LIMIT 5"))
    for row in result:
        print(row)

print("SQLAlchemy connection OK")
