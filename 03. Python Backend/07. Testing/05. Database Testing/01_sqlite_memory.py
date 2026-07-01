# 01 — SQLite in-memory for isolated DB tests
# Run: pytest 01_sqlite_memory.py -v

import sqlite3


def create_table(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY, title TEXT)")
    conn.commit()


def insert_note(conn: sqlite3.Connection, title: str) -> int:
    cur = conn.execute("INSERT INTO notes (title) VALUES (?)", (title,))
    conn.commit()
    return cur.lastrowid


def test_in_memory_db():
    conn = sqlite3.connect(":memory:")
    create_table(conn)
    note_id = insert_note(conn, "Test note")
    row = conn.execute("SELECT title FROM notes WHERE id = ?", (note_id,)).fetchone()
    conn.close()
    assert row[0] == "Test note"
