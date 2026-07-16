"""SQLite and LangChain SQLDatabase helpers."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from langchain_community.utilities import SQLDatabase

from app.config import DB_PATH


# get_connection - open a SQLite connection to the analytics database
def get_connection(db_path: Path = DB_PATH) -> sqlite3.Connection:
    """Open a SQLite connection to the analytics database."""
    if not db_path.exists():
        raise FileNotFoundError(
            f"Database not found at {db_path}. Run: python seed_db.py"
        )
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# get_sql_database - build a LangChain SQLDatabase for schema introspection
def get_sql_database(db_path: Path = DB_PATH) -> SQLDatabase:
    """Build a LangChain SQLDatabase for schema introspection."""
    uri = f"sqlite:///{db_path.resolve()}"
    return SQLDatabase.from_uri(uri)


# load_schema_map - map each table name to its column list
def load_schema_map(conn: sqlite3.Connection) -> dict[str, list[str]]:
    """Map each table name to its column list."""
    tables: dict[str, list[str]] = {}
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    ).fetchall()
    for row in rows:
        table = row[0]
        columns = [
            col[1]
            for col in conn.execute(f"PRAGMA table_info({table})").fetchall()
        ]
        tables[table] = columns
    return tables


# execute_select - run a validated SELECT and return columns plus rows
def execute_select(sql: str, conn: sqlite3.Connection) -> tuple[list[str], list[tuple]]:
    """Run a validated SELECT and return columns plus rows."""
    cursor = conn.execute(sql)
    columns = [description[0] for description in cursor.description or []]
    rows = [tuple(row) for row in cursor.fetchall()]
    return columns, rows
