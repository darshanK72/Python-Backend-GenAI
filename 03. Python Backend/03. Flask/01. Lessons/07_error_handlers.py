# 07 — Custom error responses
# Run: python 07_error_handlers.py
# Try: GET /missing   GET /boom

from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found", "detail": str(error)}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


@app.get("/")
def home():
    return {"message": "Try /missing or /boom"}


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


@app.get("/boom")
def boom():
    from flask import abort

    abort(500, description="demo failure")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
