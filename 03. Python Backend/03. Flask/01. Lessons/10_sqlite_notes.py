# 10 — Flask + SQLite (stdlib sqlite3)
# Run: python 10_sqlite_notes.py
# Creates notes_demo.db in this folder; deleted on exit if you stop the server.

import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("notes_demo.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT DEFAULT ''
            )
            """
        )


@app.get("/health")
def health():
    return {"status": "ok", "database": str(DB_PATH.name)}


@app.get("/notes")
def list_notes():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT id, title, body FROM notes ORDER BY id"
        ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.post("/notes")
def create_note():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    body = str(data.get("body", ""))
    if not title:
        return jsonify({"error": "title required"}), 400
    with get_db() as conn:
        cur = conn.execute(
            "INSERT INTO notes (title, body) VALUES (?, ?)",
            (title, body),
        )
        note_id = cur.lastrowid
        row = conn.execute(
            "SELECT id, title, body FROM notes WHERE id = ?",
            (note_id,),
        ).fetchone()
    return jsonify(dict(row)), 201


@app.delete("/notes/<int:note_id>")
def delete_note(note_id: int):
    with get_db() as conn:
        cur = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    if cur.rowcount == 0:
        return jsonify({"error": "Not found"}), 404
    return "", 204


if __name__ == "__main__":
    init_db()
    print("SQLite file:", DB_PATH)
    app.run(debug=True, port=5000)
