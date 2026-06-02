# 03 — Python Backend

Learn databases, TCP sockets, HTTP/REST, then **Flask**, **FastAPI**, and **Django**.

```bash
# repo root
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy [`config.example.env`](config.example.env) to repo root `.env` for MySQL lessons.

## Learning path

| Order | Folder | Topics |
|-------|--------|--------|
| 1 | `01. Databases/01. SQLite/` | SQL CRUD without a server (`01`–`05`) |
| 2 | `01. Databases/02. MySQL/` | PyMySQL, transactions, helper class (`01`–`07`) |
| 3 | `02. Networking/01. Socket Programming/` | TCP server/client, echo, chat (`01`–`07`) |
| 4 | `02. Networking/02. HTTP and REST/` | HTTP, REST, JSON APIs (`01`–`04`) |
| 5 | `03. Flask/01. Lessons/` | Routes, JSON, templates, blueprints (`01`–`10`) |
| 6 | `03. Flask/02. Notes API/` | Full API: `python app.py` |
| 7 | `04. FastAPI/01. Lessons/` | Routes, Pydantic, CRUD (`01`–`05`) |
| 8 | `04. FastAPI/02. Notes API/` | Full API: `uvicorn main:app --reload` |
| 9 | `03. Django/01. Lessons/` | Concepts (`01`) |
| 10 | `03. Django/01. Todo Project/` | Django app + admin + JSON API |
| 11 | `05. Security/` | Hashing, env secrets, CORS/HTTPS |

## Quick commands

**SQLite** (no setup):
```bash
cd "01. Databases/01. SQLite"
python 01_sqlite_intro.py
```

**Flask**:
```bash
cd "03. Flask/01. Lessons"
python 02_hello.py
```

**FastAPI**:
```bash
cd "04. FastAPI/01. Lessons"
uvicorn 01_hello:app --reload --port 8000
```

**Django**:
```bash
cd "03. Django/01. Todo Project"
python manage.py migrate
python manage.py runserver
```

MySQL lessons need a running MySQL server and `learning_db` database.
