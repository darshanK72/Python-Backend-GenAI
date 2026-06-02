# 01 — Connect to MySQL with PyMySQL
# Run: python 01_connection.py
#
# Setup:
#   1. Install and start MySQL locally
#   2. Copy config.example.env to repo root .env
#   3. Create database: CREATE DATABASE learning_db;
#   4. pip install pymysql (in root requirements.txt)

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import MYSQL

try:
    import pymysql
except ImportError:
    print("Install: pip install pymysql")
    raise SystemExit(1)

try:
    conn = pymysql.connect(**MYSQL)
    print("Connected to MySQL")
    with conn.cursor() as cur:
        cur.execute("SELECT VERSION()")
        print("Server version:", cur.fetchone()[0])
    conn.close()
    print("Connection closed")
except pymysql.Error as e:
    print("MySQL error:", e)
    print("Check .env and that MySQL is running.")
