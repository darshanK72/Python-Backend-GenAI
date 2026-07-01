# 12 — Cookies
# Run: python 12_cookies.py
# GET /login sets a cookie; GET /dashboard reads it

from flask import Flask, make_response, request

app = Flask(__name__)


@app.get("/login")
def login():
    response = make_response({"message": "Logged in — check browser cookies"})
    response.set_cookie("session_id", "demo-session-123", httponly=True)
    return response


@app.get("/dashboard")
def dashboard():
    session_id = request.cookies.get("session_id")
    if not session_id:
        return {"error": "Not logged in"}, 401
    return {"session_id": session_id, "page": "dashboard"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
