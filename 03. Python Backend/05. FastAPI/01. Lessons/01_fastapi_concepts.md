# Lesson 01 — FastAPI Concepts

**Topics:** Introduction, REST architecture, framework comparison, IDE support, project layout

**Next lesson:** Run `uvicorn 02_hello:app --reload --port 8000` after reading this.

---

## What is FastAPI?

FastAPI is a modern Python web framework for building **HTTP APIs**. It is built on top of [Starlette](https://www.starlette.io/) (routing, middleware, WebSockets) and uses [Pydantic](https://docs.pydantic.dev/) for data validation and serialization.

Key characteristics:

| Feature | Why it matters |
|---------|----------------|
| **Type hints** | Route parameters, query strings, and request bodies are declared with Python types. FastAPI uses them for parsing, validation, and documentation. |
| **Automatic OpenAPI docs** | Visit `/docs` (Swagger UI) or `/redoc` without writing extra schema code. |
| **Async support** | You can write `async def` route handlers for I/O-bound work (DB, HTTP calls). Sync `def` handlers still work. |
| **High performance** | One of the fastest Python frameworks; comparable to Node and Go for many workloads. |
| **Standards-based** | OpenAPI, JSON Schema, OAuth2 patterns, and WebSockets are first-class concepts. |

FastAPI is **not** a full-stack framework like Django. It focuses on APIs. You can add Jinja2 templates and static files (lessons 12–14), but most teams pair FastAPI with a separate front end (React, Vue, mobile app).

---

## How a request flows

```
Client (browser / mobile / curl)
        │
        ▼
   ASGI server (Uvicorn)
        │
        ▼
   FastAPI app (routes, dependencies, middleware)
        │
        ├── Path / query / body parsed using type hints
        ├── Pydantic validates data → 422 if invalid
        └── Handler returns dict → JSON response
```

**ASGI** (Asynchronous Server Gateway Interface) is the successor to WSGI. Uvicorn is the ASGI server commonly used to run FastAPI in development and production.

---

## REST architecture

REST (Representational State Transfer) organizes APIs around **resources** (nouns) and **HTTP methods** (verbs).

| Method | Path example | Action |
|--------|--------------|--------|
| `GET` | `/notes` | List all notes |
| `GET` | `/notes/1` | Get one note |
| `POST` | `/notes` | Create a new note |
| `PUT` | `/notes/1` | Replace the entire note |
| `PATCH` | `/notes/1` | Partial update |
| `DELETE` | `/notes/1` | Remove the note |

**Conventions:**

- Use **plural nouns** for collections: `/users`, not `/getUsers`.
- Put identifiers in the **path**: `/users/42`, not `/users?id=42` for a single resource.
- Return **JSON** for API responses in most cases.
- Use **status codes** to communicate outcome:
  - `200` OK — success with body
  - `201` Created — resource created
  - `204` No Content — success, no body (common for DELETE)
  - `400` Bad Request — client sent invalid data
  - `401` Unauthorized — authentication required
  - `403` Forbidden — authenticated but not allowed
  - `404` Not Found — resource does not exist
  - `422` Unprocessable Entity — validation failed (FastAPI default for bad input)
  - `500` Internal Server Error — server bug

FastAPI lessons 05–07 cover path and query parameters; lesson 09 covers request bodies; lesson 20 builds a full in-memory CRUD API.

---

## FastAPI vs Flask vs Django

| | **Flask** | **Django** | **FastAPI** |
|---|-----------|------------|-------------|
| **Style** | Microframework | Batteries-included | API-focused, async-ready |
| **Validation** | Manual or extensions | Forms / DRF serializers | Pydantic built in |
| **API docs** | Manual or Swagger extension | DRF has schema tools | Auto-generated OpenAPI |
| **ORM** | You choose (SQLAlchemy, etc.) | Django ORM included | You choose (SQLAlchemy, etc.) |
| **Admin UI** | No | Yes (`/admin`) | No |
| **Templates** | Jinja2 common | Django templates | Jinja2 optional |
| **Async** | Limited (Flask 2+ has some support) | Django 4+ ASGI | Native `async def` |
| **Best for** | Small apps, learning, custom stacks | Full web apps, CMS, admin-heavy sites | REST/JSON APIs, microservices |

**When to pick FastAPI:**

- Building a JSON API for a SPA or mobile app
- You want automatic interactive docs (`/docs`)
- Type safety and validation matter
- You need async I/O (many DB/HTTP calls)

**When Flask or Django might fit better:**

- Flask — minimal API, existing Flask ecosystem, very small services
- Django — admin panel, built-in auth, server-rendered HTML as the main UI

---

## IDE support and type hints

FastAPI is designed around Python **type hints**. When you write:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int, active: bool = True):
    ...
```

the IDE (VS Code, PyCharm, Cursor with Pylance) can:

- Autocomplete parameter names and types
- Flag type errors before you run the app
- Show inline documentation from docstrings in `/docs`

Enable **Pylance** or run **mypy** in CI for stronger static checking. Lesson 04 demonstrates how FastAPI uses types for parsing and documentation.

---

## Typical project layout

For small tutorials, a single `main.py` is enough. For real projects:

```
my_api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI() instance, middleware, lifespan
│   ├── routers/
│   │   ├── notes.py         # APIRouter for /notes
│   │   └── users.py
│   ├── models/
│   │   └── schemas.py       # Pydantic models (request/response)
│   ├── services/
│   │   └── notes.py         # Business logic
│   ├── dependencies.py      # Shared Depends() functions
│   └── database.py          # DB session, engine
├── tests/
├── requirements.txt
└── .env                     # Secrets (never commit)
```

**`APIRouter`** (covered in larger projects) lets you split routes by feature and mount them with prefixes like `/api/v1/notes`.

---

## Core dependencies

Install for these lessons:

```bash
pip install fastapi "uvicorn[standard]"
```

| Package | Role |
|---------|------|
| `fastapi` | Framework |
| `uvicorn` | ASGI server |
| `pydantic` | Data validation (pulled in by FastAPI) |
| `starlette` | Low-level ASGI toolkit (pulled in by FastAPI) |

Optional extras used in later lessons:

```bash
pip install jinja2 python-multipart "pydantic[email]" motor strawberry-graphql
```

---

## Hello World preview

Lesson 02 is the first runnable app:

```python
from fastapi import FastAPI

app = FastAPI(title="Lesson 02 — Hello World")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
```

Run:

```bash
cd "05. FastAPI/01. Lessons"
uvicorn 02_hello:app --reload --port 8000
```

Open:

- API: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs

Lesson 03 explains OpenAPI and Uvicorn in more detail.

---

## Curriculum map (this folder)

| Lessons | Topic |
|---------|--------|
| 01–03 | Concepts, hello world, OpenAPI / Uvicorn |
| 04–11 | Types, parameters, Pydantic, request/response models |
| 12–15 | Templates, static files, forms, file upload |
| 16–18 | Cookies, headers, dependencies |
| 19–22 | CORS, CRUD, SQL, MongoDB |
| 23–24 | GraphQL, WebSockets |
| 25–28 | Lifespan, mounting sub-apps, middleware, Flask mount |
| 29 | Deployment overview |
| `../02. Notes API/` | Capstone project |

---

## Summary

- FastAPI builds **typed HTTP APIs** with **automatic `/docs`**.
- Design APIs with **REST** verbs and meaningful **status codes**.
- Use **Uvicorn** to run the app; use **Pydantic** models for request/response shapes.
- Prefer a **router + schemas + services** layout as projects grow.

**Next step:** `uvicorn 02_hello:app --reload --port 8000`
