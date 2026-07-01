# 07 — HTTP methods
# Run: python 07_http_methods.py
# Try: GET /items   POST /items   PUT /items/1   DELETE /items/1

from flask import Flask, jsonify, request

app = Flask(__name__)

_items: dict[int, dict] = {1: {"id": 1, "name": "pen"}}


@app.get("/items")
def list_items():
    return jsonify(list(_items.values()))


@app.post("/items")
def create_item():
    data = request.get_json(silent=True) or {}
    item_id = max(_items.keys(), default=0) + 1
    item = {"id": item_id, "name": data.get("name", "item")}
    _items[item_id] = item
    return jsonify(item), 201


@app.put("/items/<int:item_id>")
def update_item(item_id: int):
    if item_id not in _items:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json(silent=True) or {}
    _items[item_id]["name"] = data.get("name", _items[item_id]["name"])
    return jsonify(_items[item_id])


@app.delete("/items/<int:item_id>")
def delete_item(item_id: int):
    if item_id not in _items:
        return jsonify({"error": "Not found"}), 404
    del _items[item_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5000)
