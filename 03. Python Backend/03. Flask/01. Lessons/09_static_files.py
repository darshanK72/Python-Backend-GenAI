# 09 — Static files
# Run: python 09_static_files.py
# Open: http://127.0.0.1:5000/static/style.css

from flask import Flask, url_for

app = Flask(__name__)


@app.get("/")
def index():
    return {
        "message": "Static files are served from the static/ folder",
        "css_url": url_for("static", filename="style.css"),
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
