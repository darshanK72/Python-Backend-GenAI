# 08 — Jinja2 templates
# Run: python 08_templates.py
# Open: http://127.0.0.1:5000/  and  /about

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "greeting.html",
        title="Flask Templates",
        user="Learner",
        tags=["python", "flask", "jinja2"],
    )


@app.get("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
