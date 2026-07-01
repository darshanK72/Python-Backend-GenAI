# 15 — Uploading files
# Run: uvicorn 15_upload_files:app --reload --port 8000
# POST /upload  form field "file" (try from /docs)
# Install: pip install python-multipart

import shutil
from pathlib import Path

from fastapi import FastAPI, File, UploadFile

app = FastAPI(title="Lesson 15 — Upload Files")

UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@app.post("/upload")
async def upload_file(file: UploadFile = File()):
    dest = UPLOAD_DIR / file.filename
    with dest.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_to": str(dest),
    }


@app.post("/upload-multiple")
async def upload_multiple(files: list[UploadFile] = File()):
    names = [f.filename for f in files]
    return {"count": len(names), "filenames": names}
