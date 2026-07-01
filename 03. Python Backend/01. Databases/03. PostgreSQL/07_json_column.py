# 07 — JSON/JSONB column (PostgreSQL feature)
# Run: python 07_json_column.py

import json
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
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS product_meta (
                    sku TEXT PRIMARY KEY,
                    attributes JSONB NOT NULL
                )
                """
            )
            cur.execute(
                """
                INSERT INTO product_meta (sku, attributes)
                VALUES (%s, %s::jsonb)
                ON CONFLICT (sku) DO UPDATE SET attributes = EXCLUDED.attributes
                """,
                ("BOOK-01", json.dumps({"title": "Fluent Python", "tags": ["python", "advanced"]})),
            )
            cur.execute(
                """
                SELECT sku, attributes->>'title' AS title
                FROM product_meta
                WHERE attributes @> %s::jsonb
                """,
                (json.dumps({"tags": ["python"]}),),
            )
            for row in cur.fetchall():
                print(row)
        conn.commit()
    finally:
        conn.close()
