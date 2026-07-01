# 14 — Redirect and errors
# Run: python 14_redirect_errors.py
# Try: GET /old-home   GET /missing   GET /boom

from flask import Flask, abort, jsonify, redirect, url_for

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "Try /old-home, /missing, or /boom"}


@app.get("/old-home")
def old_home():
    return redirect(url_for("home"))


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found", "detail": str(error)}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


@app.get("/boom")
def boom():
    abort(500, description="demo failure")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
