# Notes API — Flask project (in-memory store)
# Run from this folder:
#   python app.py
#   # or: flask --app app run --debug --port 5000
# Endpoints: GET /health  GET/POST /notes  GET/DELETE /notes/<id>

from flask import Flask, jsonify, request

app = Flask(__name__)

_store: dict[int, dict] = {}
_next_id = 1


def _note_from_body():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    body = str(data.get("body", ""))
    if not title:
        return None, (jsonify({"error": "title required"}), 400)
    return {"title": title, "body": body}, None


@app.get("/health")
def health():
    return {"status": "ok", "framework": "flask"}


@app.get("/notes")
def list_notes():
    return jsonify(list(_store.values()))


@app.post("/notes")
def create_note():
    global _next_id
    payload, err = _note_from_body()
    if err:
        return err
    note = {"id": _next_id, **payload}
    _store[_next_id] = note
    _next_id += 1
    return jsonify(note), 201


@app.get("/notes/<int:note_id>")
def get_note(note_id: int):
    if note_id not in _store:
        return jsonify({"error": "Note not found"}), 404
    return jsonify(_store[note_id])


@app.put("/notes/<int:note_id>")
def update_note(note_id: int):
    if note_id not in _store:
        return jsonify({"error": "Note not found"}), 404
    payload, err = _note_from_body()
    if err:
        return err
    note = {"id": note_id, **payload}
    _store[note_id] = note
    return jsonify(note)


@app.delete("/notes/<int:note_id>")
def delete_note(note_id: int):
    if note_id not in _store:
        return jsonify({"error": "Note not found"}), 404
    del _store[note_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5000)
