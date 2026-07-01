# Flask app for production deploy lesson
# Run dev: python app.py

from flask import Flask, jsonify

app = Flask(__name__)
app.config["ENV"] = "production"


@app.get("/health")
def health():
    return jsonify(status="ok", runtime="flask")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
