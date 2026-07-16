"""Tests for database seeding."""

from __future__ import annotations

import sqlite3

from seed_db import create_database


# test_seed_database_counts - test seed contains required projects, tasks, members, incidents
def test_seed_database_counts(tmp_path) -> None:
    db_path = create_database(tmp_path / "analytics.db")
    conn = sqlite3.connect(db_path)
    try:
        assert conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0] == 3
        assert conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 8
        assert conn.execute("SELECT COUNT(*) FROM team_members").fetchone()[0] == 4
        assert conn.execute("SELECT COUNT(*) FROM incidents").fetchone()[0] == 3
        assert (
            conn.execute(
                "SELECT COUNT(*) FROM incidents WHERE severity = 'critical'"
            ).fetchone()[0]
            == 1
        )
        assert (
            conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'blocked'").fetchone()[0]
            >= 1
        )
    finally:
        conn.close()
