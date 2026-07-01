# 06 — URL building (url_for)
# Run: python 06_url_building.py
# Open: http://127.0.0.1:5000/  — links are built with url_for()

from flask import Flask, url_for

app = Flask(__name__)


@app.get("/")
def index():
    profile_url = url_for("profile", user_id=7)
    admin_url = url_for("admin", _external=False)
    return {
        "profile_link": profile_url,
        "admin_link": admin_url,
        "hint": "Open /profile/7 or /admin",
    }


@app.get("/profile/<int:user_id>")
def profile(user_id: int):
    return {"user_id": user_id}


@app.get("/admin")
def admin():
    return {"area": "admin"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
