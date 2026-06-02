# 06 — Blueprints (modular routes)
# Run: python 06_blueprints.py
# Try: GET /api/health   GET /api/version

from flask import Blueprint, Flask, jsonify

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/health")
def health():
    return {"status": "ok"}


@api.get("/version")
def version():
    return {"version": "1.0.0"}


app = Flask(__name__)
app.register_blueprint(api)


@app.get("/")
def root():
    return jsonify({"message": "See /api/health"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
