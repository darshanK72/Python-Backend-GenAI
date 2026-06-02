# 03 — Routes and HTTP methods
# Run: python 03_routes_and_methods.py
# Try: GET /users/42   GET /search?q=flask&limit=5

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/users/<int:user_id>")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/search")
def search():
    from flask import request

    q = request.args.get("q", "")
    limit = request.args.get("limit", 10, type=int)
    return {"query": q, "limit": limit}


@app.post("/echo")
def echo():
    from flask import request

    data = request.get_json(silent=True) or {}
    return jsonify({"received": data}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
