# 13 — Static files
# Run: uvicorn 13_static_files:app --reload --port 8000
# Open: http://127.0.0.1:8000/static/style.css

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Lesson 13 — Static Files")

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def index():
    return {"message": "Open /static/style.css for the CSS file"}
