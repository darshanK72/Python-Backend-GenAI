# 14 — HTML form templates + accessing form data
# Run: uvicorn 14_html_forms:app --reload --port 8000
# Open: http://127.0.0.1:8000/contact
# Install: pip install jinja2 python-multipart

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Lesson 14 — HTML Forms")

base = Path(__file__).parent
templates = Jinja2Templates(directory=base / "templates")
app.mount("/static", StaticFiles(directory=base / "static"), name="static")


@app.get("/contact")
def contact_form(request: Request):
    return templates.TemplateResponse(request, "contact.html", {"result": None})


@app.post("/contact")
def submit_contact(
    request: Request,
    name: str = Form(),
    email: str = Form(),
    message: str = Form(default=""),
):
    result = {"name": name, "email": email, "message": message}
    return templates.TemplateResponse(request, "contact.html", {"result": result})
