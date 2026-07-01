# 01 — Connect to PostgreSQL
# Run: python 01_connection.py
#
# Setup:
#   1. Install PostgreSQL and create database: CREATE DATABASE learning_db;
#   2. Copy config.example.env to repo root .env
#   3. pip install "psycopg[binary]"

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from db_config import POSTGRES

try:
    import psycopg
except ImportError:
    print('Install: pip install "psycopg[binary]"')
    raise SystemExit(1)


def connect():
    return psycopg.connect(
        host=POSTGRES["host"],
        port=POSTGRES["port"],
        user=POSTGRES["user"],
        password=POSTGRES["password"],
        dbname=POSTGRES["database"],
    )


if __name__ == "__main__":
    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version()")
                print("Connected to PostgreSQL")
                print("Version:", cur.fetchone()[0])
    except psycopg.Error as e:
        print("PostgreSQL error:", e)
        print("Check .env and that PostgreSQL is running.")
