# 04 — Query string, JSON body, and form data
# Run: python 04_request_data.py
# POST /items  Content-Type: application/json  body: {"name": "book", "qty": 2}

from flask import Flask, request

app = Flask(__name__)


@app.get("/items")
def list_items():
    category = request.args.get("category", "all")
    return {"category": category, "items": []}


@app.post("/items")
def create_item():
    if not request.is_json:
        return {"error": "Expected application/json"}, 400
    data = request.get_json()
    name = (data or {}).get("name", "").strip()
    qty = (data or {}).get("qty", 1)
    if not name:
        return {"error": "name required"}, 400
    return {"created": {"name": name, "qty": qty}}, 201


@app.post("/contact")
def contact_form():
    # HTML form: application/x-www-form-urlencoded
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    return {"name": name, "email": email}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
