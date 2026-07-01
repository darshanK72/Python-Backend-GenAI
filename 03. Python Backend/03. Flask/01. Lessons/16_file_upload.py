# 16 — File uploading
# Run: python 16_file_upload.py
# POST /upload  form field "file" (use curl or a simple HTML form)
# Install: no extra packages needed for basic uploads

from pathlib import Path

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@app.post("/upload")
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if not file.filename:
        return jsonify({"error": "No selected file"}), 400
    filename = secure_filename(file.filename)
    dest = UPLOAD_DIR / filename
    file.save(dest)
    return jsonify({"filename": filename, "saved_to": str(dest)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
