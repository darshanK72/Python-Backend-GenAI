# 09 — before_request hook and simple API key check
# Run: python 09_hooks_and_auth.py
# Public:  GET /
# Protected: GET /protected   Header: X-API-Key: secret-demo-key

from flask import Flask, g, jsonify, request

app = Flask(__name__)
DEMO_KEY = "secret-demo-key"


@app.before_request
def load_api_key():
    g.api_key = request.headers.get("X-API-Key", "")


def require_api_key():
    if g.api_key != DEMO_KEY:
        return jsonify({"error": "Invalid API key"}), 401
    return None


@app.get("/")
def home():
    return {"message": "Send X-API-Key header to access /protected"}


@app.get("/protected")
def protected():
    auth_error = require_api_key()
    if auth_error:
        return auth_error
    return {"message": "Access granted"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
