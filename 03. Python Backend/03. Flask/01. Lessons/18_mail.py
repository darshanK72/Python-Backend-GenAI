# 18 — Mail (configuration demo)
# Run: python 18_mail.py
# POST /send  {"to": "you@example.com", "subject": "Hi", "body": "Hello"}
# Install: pip install flask-mail
#
# This lesson shows config only — no real email is sent without SMTP credentials.

import os

from flask import Flask, jsonify, request

app = Flask(__name__)

app.config.update(
    MAIL_SERVER=os.environ.get("MAIL_SERVER", "smtp.example.com"),
    MAIL_PORT=int(os.environ.get("MAIL_PORT", "587")),
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME", ""),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD", ""),
    MAIL_DEFAULT_SENDER=os.environ.get("MAIL_DEFAULT_SENDER", "noreply@example.com"),
)

try:
    from flask_mail import Mail, Message

    mail = Mail(app)
    HAS_MAIL = True
except ImportError:
    mail = None
    HAS_MAIL = False


@app.get("/mail/config")
def mail_config():
    return {
        "flask_mail_installed": HAS_MAIL,
        "server": app.config["MAIL_SERVER"],
        "port": app.config["MAIL_PORT"],
        "hint": "Set MAIL_* env vars and call /send to dispatch email",
    }


@app.post("/send")
def send_mail():
    if not HAS_MAIL:
        return jsonify({"error": "pip install flask-mail"}), 503
    data = request.get_json(silent=True) or {}
    to_addr = data.get("to")
    if not to_addr:
        return jsonify({"error": "to address required"}), 400
    if not app.config["MAIL_USERNAME"]:
        return jsonify({
            "error": "MAIL_USERNAME not set — configure SMTP env vars first",
            "would_send": data,
        }), 503
    msg = Message(
        subject=data.get("subject", "Hello from Flask"),
        recipients=[to_addr],
        body=data.get("body", ""),
    )
    mail.send(msg)
    return jsonify({"sent": True, "to": to_addr})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
