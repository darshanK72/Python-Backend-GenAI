# 10 — Request object
# Run: python 10_request_object.py
# GET /search?q=flask&limit=5
# POST /items  Content-Type: application/json  {"name": "book", "qty": 2}
# POST /contact  form fields name, email

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/search")
def search():
    return {
        "query": request.args.get("q", ""),
        "limit": request.args.get("limit", 10, type=int),
        "method": request.method,
    }


@app.post("/items")
def create_item():
    if not request.is_json:
        return jsonify({"error": "Expected application/json"}), 400
    data = request.get_json()
    name = (data or {}).get("name", "").strip()
    if not name:
        return jsonify({"error": "name required"}), 400
    return jsonify({"created": {"name": name, "qty": data.get("qty", 1)}}), 201


@app.post("/contact")
def contact_form():
    return {
        "name": request.form.get("name", ""),
        "email": request.form.get("email", ""),
        "content_type": request.content_type,
    }


@app.get("/headers")
def show_headers():
    return {
        "user_agent": request.headers.get("User-Agent"),
        "accept": request.headers.get("Accept"),
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
