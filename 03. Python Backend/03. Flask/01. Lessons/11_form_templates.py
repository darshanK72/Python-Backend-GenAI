# 11 — Sending form data to a template
# Run: python 11_form_templates.py
# Open: http://127.0.0.1:5000/contact

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/contact")
def contact_form():
    return render_template("contact.html", submitted=False)


@app.post("/contact")
def submit_contact():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")
    return render_template(
        "contact.html",
        submitted=True,
        name=name,
        email=email,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
