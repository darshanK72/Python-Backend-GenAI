# 23 — AJAX (modern alternative to Sijax)
# Run: python 23_ajax.py
# Open: http://127.0.0.1:5000/  — click "Load greeting"
#
# Sijax was a Flask extension for AJAX callbacks. Today, fetch() + JSON APIs
# is the standard approach (same pattern as SPA front ends).

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("ajax_demo.html")


@app.get("/api/greeting")
def greeting():
    return jsonify({"message": "Hello from Flask API!", "framework": "flask"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
