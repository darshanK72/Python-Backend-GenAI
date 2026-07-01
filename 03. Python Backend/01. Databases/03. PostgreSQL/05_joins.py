# 05 — JOIN two tables
# Run: python 05_joins.py

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
                CREATE TABLE IF NOT EXISTS department (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL UNIQUE
                )
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS employee (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL UNIQUE,
                    dept_id INTEGER REFERENCES department(id)
                )
                """
            )
            cur.execute(
                """
                INSERT INTO department (name) VALUES ('IT'), ('HR')
                ON CONFLICT (name) DO NOTHING
                """
            )
            cur.execute("SELECT id FROM department WHERE name = 'IT'")
            it_id = cur.fetchone()[0]
            cur.execute("SELECT id FROM department WHERE name = 'HR'")
            hr_id = cur.fetchone()[0]
            cur.execute(
                """
                INSERT INTO employee (name, dept_id) VALUES
                    ('Asha', %s), ('Ravi', %s)
                ON CONFLICT (name) DO NOTHING
                """,
                (it_id, hr_id),
            )
            cur.execute(
                """
                SELECT e.name, d.name AS department
                FROM employee e
                INNER JOIN department d ON e.dept_id = d.id
                ORDER BY e.name
                """
            )
            for row in cur.fetchall():
                print(row)
        conn.commit()
    finally:
        conn.close()
