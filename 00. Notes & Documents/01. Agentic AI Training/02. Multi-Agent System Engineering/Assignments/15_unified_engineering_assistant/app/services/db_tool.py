"""SQLite query helper for the MCP db_query tool."""

from __future__ import annotations

import re
import sqlite3

from langchain_community.utilities import SQLDatabase

from app.config import DB_PATH
from app.services.llm_service import LLMService
from app.services.sql_parser import extract_sql

# SQL_SYSTEM - instruct the LLM to emit a single SELECT only
SQL_SYSTEM = """You write SQLite SELECT queries for project management analytics.
Return only one SELECT statement. Never use DDL or DML."""


# db_query - answer a natural-language project question against SQLite
def db_query(question: str, *, service: LLMService | None = None) -> str:
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found at {DB_PATH}. Run: python seed_db.py"
        )
    llm = service or LLMService()
    sql_db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH.resolve()}")
    schema = sql_db.get_table_info()
    sql = extract_sql(
        llm.chat(
            [
                {"role": "system", "content": SQL_SYSTEM},
                {
                    "role": "user",
                    "content": f"Schema:\n{schema}\n\nQuestion: {question}",
                },
            ],
            temperature=0.0,
        )
    )
    if not sql.upper().startswith("SELECT"):
        return "Only SELECT queries are permitted."
    if re.search(r"\b(DROP|DELETE|UPDATE|INSERT|ALTER|CREATE)\b", sql, re.I):
        return "Only SELECT queries are permitted."

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.execute(sql)
        columns = [description[0] for description in cursor.description or []]
        rows = cursor.fetchall()
    except sqlite3.Error as exc:
        return f"SQL error: {exc}"
    finally:
        conn.close()

    summary = llm.chat(
        [
            {
                "role": "user",
                "content": (
                    f"Question: {question}\nSQL: {sql}\nColumns: {columns}\nRows: {rows}\n"
                    "Write one plain-English answer sentence."
                ),
            }
        ],
        temperature=0.2,
    ).strip()
    return summary
