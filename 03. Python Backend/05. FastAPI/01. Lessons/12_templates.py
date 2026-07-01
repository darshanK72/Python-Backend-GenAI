# 12 — Jinja2 templates
# Run: uvicorn 12_templates:app --reload --port 8000
# Open: http://127.0.0.1:8000/
# Install: pip install jinja2

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Lesson 12 — Templates")

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "greeting.html",
        {
            "title": "FastAPI Templates",
            "user": "Learner",
            "tags": ["python", "fastapi", "jinja2"],
        },
    )
