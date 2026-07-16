"""Create and seed the project management SQLite database."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from app.config import DB_PATH

# SCHEMA_SQL - DDL for the Assignment 10 project_management schema
SCHEMA_SQL = """
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT CHECK(status IN ('planning','active','on_hold','completed','cancelled')),
    priority TEXT CHECK(priority IN ('low','medium','high','critical')),
    start_date DATE, due_date DATE, team_lead TEXT, budget_usd INTEGER
);
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER REFERENCES projects(id),
    title TEXT NOT NULL,
    status TEXT CHECK(status IN ('todo','in_progress','review','done','blocked')),
    assignee TEXT, story_points INTEGER, due_date DATE
);
CREATE TABLE team_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, role TEXT, department TEXT,
    email TEXT UNIQUE, hourly_rate INTEGER, skills TEXT
);
CREATE TABLE incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,
    severity TEXT CHECK(severity IN ('critical','high','medium','low')),
    project_id INTEGER REFERENCES projects(id),
    reporter TEXT, assigned_to TEXT, description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


# seed_database - insert realistic projects, tasks, members, and incidents
def seed_database(conn: sqlite3.Connection) -> None:
    """Insert the assignment seed rows into an empty database."""
    projects = [
        (
            "Customer Self-Service Portal Modernisation",
            "active",
            "high",
            "2025-01-10",
            "2025-06-30",
            "Carol Smith",
            120000,
        ),
        (
            "Enterprise Event Streaming and Analytics Pipeline",
            "active",
            "critical",
            "2025-02-01",
            "2025-08-15",
            "Carol Smith",
            95000,
        ),
        (
            "Field Technician Mobile Companion App",
            "on_hold",
            "medium",
            "2024-11-01",
            "2025-05-01",
            "Bob Kumar",
            80000,
        ),
    ]
    conn.executemany(
        """
        INSERT INTO projects (name, status, priority, start_date, due_date, team_lead, budget_usd)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        projects,
    )

    tasks = [
        (
            1,
            "Rebuild SSO login experience with OAuth callback and session hardening",
            "in_progress",
            "Alice Chen",
            5,
            "2025-04-01",
        ),
        (
            1,
            "Ship admin dashboard CSV export for filtered reports and audit downloads",
            "todo",
            "Bob Kumar",
            3,
            "2025-04-15",
        ),
        (
            1,
            "Investigate and fix premature session expiry blocking portal checkout flows",
            "blocked",
            "Alice Chen",
            2,
            "2025-03-20",
        ),
        (
            2,
            "Implement nightly batch ingestion job from CRM exports into the analytics warehouse",
            "review",
            "Bob Kumar",
            8,
            "2025-05-01",
        ),
        (
            2,
            "Add exponential-backoff retry and dead-letter handling for failed ingestion batches",
            "blocked",
            "Dana Lopez",
            3,
            "2025-04-10",
        ),
        (
            2,
            "Complete warehouse schema migration for event_facts and dimension tables",
            "done",
            "Alice Chen",
            5,
            "2025-03-01",
        ),
        (
            3,
            "Spike Firebase vs Azure Notification Hubs for technician push alerts",
            "todo",
            "Dana Lopez",
            2,
            "2025-05-15",
        ),
        (
            3,
            "Prototype offline work-order sync with conflict resolution for field devices",
            "in_progress",
            "Bob Kumar",
            5,
            "2025-06-01",
        ),
    ]
    conn.executemany(
        """
        INSERT INTO tasks (project_id, title, status, assignee, story_points, due_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        tasks,
    )

    members = [
        (
            "Alice Chen",
            "Senior Backend Engineer",
            "Engineering",
            "alice@example.com",
            85,
            "python,fastapi,sql,oauth",
        ),
        (
            "Bob Kumar",
            "Full-Stack Engineer",
            "Engineering",
            "bob@example.com",
            80,
            "python,react,typescript,data-pipelines",
        ),
        (
            "Carol Smith",
            "Engineering Lead",
            "Engineering",
            "carol@example.com",
            110,
            "system-architecture,sql,delivery-management",
        ),
        (
            "Dana Lopez",
            "QA Automation Engineer",
            "Quality",
            "dana@example.com",
            75,
            "pytest,playwright,ci-cd,observability",
        ),
    ]
    conn.executemany(
        """
        INSERT INTO team_members (name, role, department, email, hourly_rate, skills)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        members,
    )

    incidents = [
        (
            "Critical overnight CRM ingestion outage halted warehouse refresh",
            "critical",
            2,
            "Alice Chen",
            "Bob Kumar",
            "The scheduled 02:00 UTC CRM export ingestion failed after an upstream schema change. "
            "Zero event_facts rows landed for 14 hours, blocking morning exec dashboards and SLA "
            "reporting. Need hotfix adapter mapping plus replay of the missed batches.",
        ),
        (
            "Portal login P95 latency exceeded 2.5s during peak traffic",
            "high",
            1,
            "Dana Lopez",
            "Alice Chen",
            "Synthetic checks and real-user monitoring show OAuth redirect and session creation "
            "crossing the 1.5s SLO between 09:00–11:00 IST. Suspect Redis connection pool "
            "exhaustion under concurrent SSO callbacks; requires load-test evidence and a fix.",
        ),
        (
            "Mobile CI producing installable builds older than the release branch HEAD",
            "low",
            3,
            "Bob Kumar",
            "Dana Lopez",
            "The field-app nightly pipeline published an APK from a cached commit six days behind "
            "develop. Installers were marked 'latest' in Artifacts, causing QA to validate stale "
            "offline-sync changes. Cache key / branch filter in the workflow needs correction.",
        ),
    ]
    conn.executemany(
        """
        INSERT INTO incidents (title, severity, project_id, reporter, assigned_to, description)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        incidents,
    )


# create_database - recreate and seed project_management.db
def create_database(db_path: Path = DB_PATH) -> Path:
    """Recreate and seed the SQLite database at db_path."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(SCHEMA_SQL)
        seed_database(conn)
        conn.commit()
    finally:
        conn.close()
    return db_path


# main - seed the SQLite database used by db_query
def main() -> int:
    """Recreate and seed project_management.db for evaluators."""
    path = create_database()
    print(f"Created and seeded database at {path}")
    return 0


# main - run the database seed CLI
if __name__ == "__main__":
    raise SystemExit(main())
