# 20 — JSON CRUD API (in-memory)
# Run: python 20_json_crud.py
#   GET    /notes
#   POST   /notes   {"title": "Learn Flask", "body": "..."}
#   PUT    /notes/1
#   DELETE /notes/1

from flask import Flask, jsonify, request

app = Flask(__name__)

_notes: dict[int, dict] = {}
_next_id = 1


def _parse_note_body():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    body = str(data.get("body", ""))
    if not title:
        return None, (jsonify({"error": "title required"}), 400)
    return {"title": title, "body": body}, None


@app.get("/notes")
def list_notes():
    return jsonify(list(_notes.values()))


@app.get("/notes/<int:note_id>")
def get_note(note_id: int):
    if note_id not in _notes:
        return jsonify({"error": "Not found"}), 404
    return jsonify(_notes[note_id])


@app.post("/notes")
def create_note():
    global _next_id
    payload, err = _parse_note_body()
    if err:
        return err
    note = {"id": _next_id, **payload}
    _notes[_next_id] = note
    _next_id += 1
    return jsonify(note), 201


@app.put("/notes/<int:note_id>")
def update_note(note_id: int):
    if note_id not in _notes:
        return jsonify({"error": "Not found"}), 404
    payload, err = _parse_note_body()
    if err:
        return err
    note = {"id": note_id, **payload}
    _notes[note_id] = note
    return jsonify(note)


@app.delete("/notes/<int:note_id>")
def delete_note(note_id: int):
    if note_id not in _notes:
        return jsonify({"error": "Not found"}), 404
    del _notes[note_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5000)
