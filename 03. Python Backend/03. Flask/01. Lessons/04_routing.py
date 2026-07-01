# 04 — Routing
# Run: python 04_routing.py
# Try: GET /   GET /about   GET /api/status

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {"page": "home"}


@app.route("/about")
def about():
    return {"page": "about"}


@app.route("/api/status")
def status():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
