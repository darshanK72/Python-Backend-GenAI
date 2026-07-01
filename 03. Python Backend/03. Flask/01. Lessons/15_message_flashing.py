# 15 — Message flashing
# Run: python 15_message_flashing.py
# Open: http://127.0.0.1:5000/login
# Login with username=demo  password=secret

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "lesson-demo-secret-change-in-production"


@app.get("/login")
def login_form():
    return render_template("login.html")


@app.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    if username == "demo" and password == "secret":
        flash("Welcome back!", "success")
        return redirect(url_for("dashboard"))
    flash("Invalid username or password", "error")
    return redirect(url_for("login_form"))


@app.get("/dashboard")
def dashboard():
    return {"message": "You reached the dashboard (see flash on /login)"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
