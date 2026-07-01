# 03 — Flask application (Hello World)
# Run: python 03_hello.py
# Open: http://127.0.0.1:5000/
# Or:  flask --app 03_hello run --debug --port 5000

from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
