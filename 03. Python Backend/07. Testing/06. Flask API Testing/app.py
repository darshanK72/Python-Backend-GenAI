# Mini Flask app for testing lessons
# Run: python app.py  (optional manual check)

from flask import Flask, jsonify, request

app = Flask(__name__)
_store: list[dict] = []
_next_id = 1


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/notes")
def list_notes():
    return jsonify(_store)


@app.post("/notes")
def create_note():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify(error="title required"), 400
    global _next_id
    note = {"id": _next_id, "title": title}
    _store.append(note)
    _next_id += 1
    return jsonify(note), 201


if __name__ == "__main__":
    app.run(port=5001, debug=True)
