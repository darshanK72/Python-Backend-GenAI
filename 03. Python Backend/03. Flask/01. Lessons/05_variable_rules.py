# 05 — Variable rules (dynamic URL segments)
# Run: python 05_variable_rules.py
# Try: GET /users/42   GET /posts/2024/flask-intro   GET /path/home/docs

from flask import Flask

app = Flask(__name__)


@app.get("/users/<int:user_id>")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/posts/<int:year>/<slug>")
def get_post(year: int, slug: str):
    return {"year": year, "slug": slug}


@app.get("/path/<path:subpath>")
def catch_path(subpath: str):
    return {"subpath": subpath}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
