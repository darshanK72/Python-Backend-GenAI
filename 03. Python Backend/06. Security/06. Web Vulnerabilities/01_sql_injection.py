# 01 — SQL injection: unsafe vs parameterized queries
# Run: python 01_sql_injection.py

import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("_demo.db")


def setup():
    if DB.exists():
        DB.unlink()
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
    conn.execute("INSERT INTO users (username) VALUES ('alice')")
    conn.commit()
    conn.close()


def unsafe_lookup(username: str) -> list:
    conn = sqlite3.connect(DB)
    # NEVER do this — attacker can pass: ' OR '1'='1
    query = f"SELECT id, username FROM users WHERE username = '{username}'"
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows


def safe_lookup(username: str) -> list:
    conn = sqlite3.connect(DB)
    rows = conn.execute(
        "SELECT id, username FROM users WHERE username = ?",
        (username,),
    ).fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    setup()
    attack = "' OR '1'='1"
    print("Unsafe rows returned:", len(unsafe_lookup(attack)))
    print("Safe rows returned:", len(safe_lookup(attack)))
    DB.unlink(missing_ok=True)
