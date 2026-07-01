# 19 — Flask-WTF (forms + CSRF)
# Run: python 19_wtf_forms.py
# Open: http://127.0.0.1:5000/
# Install: pip install flask-wtf

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "lesson-demo-secret-change-in-production"


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Send")


@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    success = False
    name = ""
    if form.validate_on_submit():
        success = True
        name = form.name.data
    return render_template("wtf_contact.html", form=form, success=success, name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
