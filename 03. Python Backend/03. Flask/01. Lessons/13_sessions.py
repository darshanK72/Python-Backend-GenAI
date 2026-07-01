# 13 — Sessions (server-side, signed cookie)
# Run: python 13_sessions.py
# POST /login  form: username=demo&password=secret
# GET /profile

from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = "lesson-demo-secret-change-in-production"


@app.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    if username == "demo" and password == "secret":
        session["user"] = username
        return jsonify({"message": "Logged in", "user": username})
    return jsonify({"error": "Invalid credentials"}), 401


@app.get("/profile")
def profile():
    user = session.get("user")
    if not user:
        return jsonify({"error": "Not logged in"}), 401
    return jsonify({"user": user})


@app.post("/logout")
def logout():
    session.pop("user", None)
    return jsonify({"message": "Logged out"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
