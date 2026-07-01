# Service + repository for integration test demo

import sqlite3


class NoteRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT)")
        self.conn.commit()

    def add(self, title: str) -> int:
        cur = self.conn.execute("INSERT INTO notes (title) VALUES (?)", (title,))
        self.conn.commit()
        return cur.lastrowid

    def count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]


class NoteAppService:
    def __init__(self, repo: NoteRepository):
        self.repo = repo

    def create_note(self, title: str) -> dict:
        if not title.strip():
            raise ValueError("title required")
        note_id = self.repo.add(title.strip())
        return {"id": note_id, "title": title.strip()}

    def stats(self) -> dict:
        return {"total": self.repo.count()}
