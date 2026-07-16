"""Tests for seeding."""

import sqlite3

from seed_db import create_database


def test_seed_database(tmp_path) -> None:
    db_path = create_database(tmp_path / "project_management.db")
    conn = sqlite3.connect(db_path)
    try:
        assert conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 8
        assert (
            conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'blocked'").fetchone()[0]
            == 2
        )
    finally:
        conn.close()
