# 01 — FastAPI concepts (read-only)
# Run: python 01_fastapi_concepts.py
#
# Topics: Introduction, REST architecture, IDE support

# --- What is FastAPI? ---
# FastAPI is a modern, async-capable Python web framework for building APIs.
# It uses standard Python type hints and Pydantic for validation and
# automatically generates OpenAPI (Swagger) documentation.

# --- REST architecture ---
# REST uses HTTP methods on resources (nouns), not actions (verbs):
#   GET    /notes       -> list notes
#   GET    /notes/1     -> get one note
#   POST   /notes       -> create
#   PUT    /notes/1     -> replace
#   PATCH  /notes/1     -> partial update
#   DELETE /notes/1     -> remove
# Responses are usually JSON; status codes carry meaning (200, 201, 404, etc.).

# --- FastAPI vs Flask vs Django ---
# Flask   -> microframework, sync-first, manual validation
# Django  -> full stack with ORM, admin, templates
# FastAPI -> async-ready, Pydantic validation, auto OpenAPI docs

# --- IDE support ---
# Type hints on path/query/body parameters give autocomplete and inline errors
# in VS Code, PyCharm, and Cursor when Pylance or mypy is enabled.

# --- Typical layout ---
#   main.py or app/ package
#   routers/          # APIRouter per feature
#   models/           # Pydantic schemas
#   dependencies.py   # shared Depends() logic

if __name__ == "__main__":
    print("FastAPI builds typed HTTP APIs with automatic /docs.")
    print("Next: uvicorn 02_hello:app --reload --port 8000")
