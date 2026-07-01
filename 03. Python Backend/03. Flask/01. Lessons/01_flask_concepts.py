# 01 — Flask overview (read-only)
# Run: python 01_flask_concepts.py
#
# Topics: What is Flask, Werkzeug, Jinja2, microframework idea

# --- What is Flask? ---
# Flask is a lightweight WSGI web framework. You add only what you need
# (routing, templates, sessions) instead of a full batteries-included stack.

# --- Core building blocks ---
# Werkzeug  -> HTTP utilities, routing, request/response objects
# Jinja2    -> HTML templates with {{ variables }} and {% blocks %}
# Flask     -> thin layer tying them together

# --- Flask vs Django vs FastAPI ---
# Django  -> full framework: ORM, admin, auth, templates built in
# Flask   -> microframework: small core, you pick extensions (SQLAlchemy, etc.)
# FastAPI -> async-first, automatic OpenAPI docs, Pydantic validation

# --- Typical project layout ---
#   app.py              # create_app() or Flask(__name__)
#   routes/             # blueprints per feature
#   templates/          # Jinja2 HTML
#   static/             # CSS, JS, images

# --- How to run lessons in this folder ---
#   cd "03. Flask/01. Lessons"
#   .venv\Scripts\activate
#   pip install -r requirements.txt
#   python 03_hello.py

if __name__ == "__main__":
    print("Flask is a microframework for HTTP APIs and small web apps.")
    print("Next: python 02_environment.py  then  python 03_hello.py")
