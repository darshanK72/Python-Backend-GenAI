# 01 — Flask concepts (read-only)
# Run: python 01_flask_concepts.py

# --- 1. What is Flask? ---
# Flask is a lightweight WSGI web framework. You add only what you need
# (routing, templates, sessions) instead of a full batteries-included stack.

# --- 2. Flask vs Django vs FastAPI ---
# Django  -> full framework: ORM, admin, auth, templates built in
# Flask   -> microframework: small core, you pick extensions (SQLAlchemy, etc.)
# FastAPI -> async-first, automatic OpenAPI docs, Pydantic validation

# --- 3. Typical project layout ---
#   app.py              # create_app() or Flask(__name__)
#   routes/             # blueprints per feature
#   templates/          # Jinja2 HTML
#   static/             # CSS, JS, images

# --- 4. How to run lessons in this folder ---
#   pip install flask
#   python 02_hello.py
#   # or: flask --app 02_hello run --debug --port 5000

if __name__ == "__main__":
    print("Flask is a microframework for HTTP APIs and small web apps.")
    print("Next: python 02_hello.py  then open http://127.0.0.1:5000/")
