# 03 — Python Backend

Learn databases, TCP sockets, HTTP/REST, then **Flask**, **FastAPI**, and **Django**.

```bash
# repo root
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy [`config.example.env`](config.example.env) to repo root `.env` for MySQL, PostgreSQL, MongoDB, and Redis.

## Learning path

| Order | Folder | Topics |
|-------|--------|--------|
| 1 | `01. Databases/01. SQLite/` | SQL CRUD without a server (`01`–`05`) |
| 2 | `01. Databases/02. MySQL/` | PyMySQL, transactions, helper class (`01`–`07`) |
| 3 | `01. Databases/03. PostgreSQL/` | psycopg connect, CRUD, JSONB (`01`–`07`) |
| 4 | `01. Databases/04. SQLAlchemy/` | Engine, ORM, relationships (`01`–`07`) |
| 5 | `01. Databases/05. MongoDB/` | Documents, queries, aggregation (`01`–`05`) |
| 6 | `01. Databases/06. Redis/` | Strings, lists, hashes, cache (`01`–`06`) |
| 7 | `01. Databases/07. Alembic/` | Migrations upgrade/downgrade (`01`–`06`) |
| 8 | `02. Networking/01. Socket Programming/` | TCP, IP/DNS, SSL socket, troubleshooting (`01`–`10`) |
| 9 | `02. Networking/02. HTTP and REST/` | HTTP, REST, HTTPS, advanced client (`01`–`07`) |
| 10 | `02. Networking/03. UDP Programming/` | UDP server/client, echo (`01`–`04`) |
| 11 | `02. Networking/04. WebSockets/` | WS server/client, chat (`01`–`03`) |
| 12 | `02. Networking/05. GraphQL/` | Schema, server, queries, mutations (`01`–`05`) |
| 13 | `02. Networking/06. Server-Sent Events/` | SSE server/client, FastAPI stream (`01`–`03`) |
| 14 | `02. Networking/07. gRPC/` | proto, server, client (`01`–`03`) |
| 15 | `02. Networking/08. Message Queues/` | Redis pub/sub, RabbitMQ (`01`–`03`) |
| 16 | `03. Flask/01. Lessons/` | Full Flask curriculum (`01`–`26`) |
| 17 | `03. Flask/02. Notes API/` | Full API: `python app.py` |
| 18 | `05. FastAPI/01. Lessons/` | Full FastAPI curriculum (`01`–`29`) |
| 19 | `05. FastAPI/02. Notes API/` | Full API: `uvicorn main:app --reload` |
| 20 | `04. Django/01. Lessons/` | Runnable Django lessons (`01`–`26`) |
| 21 | `04. Django/01. Todo Project/` | Capstone: admin + JSON API |
| 22 | `06. Security/01. Passwords and Hashing/` | PBKDF2, bcrypt, timing-safe compare (`01`–`03`) |
| 23 | `06. Security/02. Secrets and Configuration/` | Env vars, dotenv, git hygiene (`01`–`03`) |
| 24 | `06. Security/03. Transport Security/` | HTTPS, CORS, security headers (`01`–`03`) |
| 25 | `06. Security/04. Authentication/` | API keys, JWT, sessions vs tokens (`01`–`03`) |
| 26 | `06. Security/05. Authorization/` | RBAC, IDOR, permissions (`01`–`03`) |
| 27 | `06. Security/06. Web Vulnerabilities/` | SQLi, XSS, CSRF, validation (`01`–`04`) |
| 28 | `06. Security/07. API Security/` | Rate limits, webhooks, API key FastAPI (`01`–`03`) |
| 29 | `06. Security/08. Cryptography Basics/` | Hash vs encrypt, Fernet, HMAC (`01`–`03`) |
| 30 | `06. Security/09. Cookies and Sessions/` | Cookie flags, session lifecycle (`01`–`02`) |
| 31 | `06. Security/10. File Upload Security/` | Safe filenames, validation (`01`–`02`) |
| 32 | `06. Security/11. Secure Coding Practices/` | Safe logging, errors, pinning (`01`–`03`) |
| 33 | `06. Security/12. Security Scanning/` | Bandit, pip-audit (`01`–`02`) |
| 34 | `06. Security/13. Production Hardening/` | Checklist, TLS proxy, prod settings (`01`–`03`) |
| 35 | `06. Security/14. Security Capstone/` | Secure Notes API (`01`–`02`) |
| 36 | `07. Testing/01. Backend Testing Overview/` | Pyramid, AAA, checklist (`01`–`03`) |
| 37 | `07. Testing/02. pytest Project Setup/` | Discovery, conftest, markers (`01`–`03`) |
| 38 | `07. Testing/03. Unit Testing Services/` | Service layer tests (`01`) |
| 39 | `07. Testing/04. Mocking External Dependencies/` | Mock, patch (`01`–`02`) |
| 40 | `07. Testing/05. Database Testing/` | SQLite, SQLAlchemy, rollback (`01`–`03`) |
| 41 | `07. Testing/06. Flask API Testing/` | Flask test client (`01`–`02`) |
| 42 | `07. Testing/07. FastAPI Testing/` | TestClient, overrides, 422 (`01`–`03`) |
| 43 | `07. Testing/08. Django API Testing/` | Django Client, TestCase (`01`–`02`) |
| 44 | `07. Testing/09. Authentication Testing/` | Auth service, protected routes (`01`–`02`) |
| 45 | `07. Testing/10. Integration Testing/` | Service + DB stack (`01`–`02`) |
| 46 | `07. Testing/11. Async API Testing/` | pytest-asyncio + httpx (`01`) |
| 47 | `07. Testing/12. Fixtures and Factories/` | Factories, fixture builders (`01`–`02`) |
| 48 | `07. Testing/13. Coverage and CI/` | Coverage, CI, GitHub Actions (`01`–`03`) |
| 49 | `07. Testing/14. Testing Capstone/` | Full Notes API test suite (`01`–`02`) |
| 50 | `08. Deployment & DevOps/01. Twelve-Factor and Environment/` | 12-factor, stages, pydantic-settings (`01`–`03`) |
| 51 | `08. Deployment & DevOps/02. WSGI and ASGI Servers/` | Uvicorn, Gunicorn workers (`01`–`03`) |
| 52 | `08. Deployment & DevOps/03. Docker Basics/` | Dockerfile, build/run (`01`) |
| 53 | `08. Deployment & DevOps/04. Docker Compose/` | Multi-service stack (`01`) |
| 54 | `08. Deployment & DevOps/05. Reverse Proxy and TLS/` | Nginx, Caddy, TLS checklist (`01`–`03`) |
| 55 | `08. Deployment & DevOps/06. Production FastAPI Deploy/` | Prod settings, graceful shutdown (`01`–`02`) |
| 56 | `08. Deployment & DevOps/07. Production Flask Deploy/` | Waitress, Gunicorn (`01`–`02`) |
| 57 | `08. Deployment & DevOps/08. Production Django Deploy/` | Gunicorn, ASGI, checklist (`01`–`03`) |
| 58 | `08. Deployment & DevOps/09. CI CD Pipelines/` | GitHub Actions, test gate, strategies (`01`–`03`) |
| 59 | `08. Deployment & DevOps/10. Health Checks and Graceful Shutdown/` | Liveness, readiness, signals (`01`–`02`) |
| 60 | `08. Deployment & DevOps/11. Deployment Capstone/` | Dockerized Notes API (`01`) |
| 61 | `09. Background Jobs & Serverless Functions/01. Sync vs Async Work/` | When to queue (`01`–`02`) |
| 62 | `09. Background Jobs & Serverless Functions/02. Threading and Process Workers/` | Thread/process pools (`01`–`02`) |
| 63 | `09. Background Jobs & Serverless Functions/03. RQ with Redis/` | Enqueue jobs (`01`–`02`) |
| 64 | `09. Background Jobs & Serverless Functions/04. Celery Basics/` | Celery app, tasks (`01`–`02`) |
| 65 | `09. Background Jobs & Serverless Functions/05. Celery with RabbitMQ/` | Broker comparison (`01`–`02`) |
| 66 | `09. Background Jobs & Serverless Functions/06. Scheduled and Periodic Tasks/` | APScheduler, Celery Beat (`01`–`02`) |
| 67 | `09. Background Jobs & Serverless Functions/07. Task Retries and Idempotency/` | Retry, idempotent tasks (`01`–`03`) |
| 68 | `09. Background Jobs & Serverless Functions/08. AWS Lambda Basics/` | Handler, Mangum (`01`–`02`) |
| 69 | `09. Background Jobs & Serverless Functions/09. Azure Functions/` | HTTP + queue triggers (`01`–`02`) |
| 70 | `09. Background Jobs & Serverless Functions/10. Google Cloud Functions/` | HTTP + Pub/Sub (`01`–`02`) |
| 71 | `09. Background Jobs & Serverless Functions/11. Serverless vs Containers/` | Decision guide (`01`–`02`) |
| 72 | `09. Background Jobs & Serverless Functions/12. Background Jobs Capstone/` | Signup + job queue API (`01`) |
| 73 | `10. Logging & Observability/01. Python Logging Basics/` | Levels, handlers (`01`–`03`) |
| 74 | `10. Logging & Observability/02. Structured JSON Logging/` | JSON formatter, fields (`01`–`02`) |
| 75 | `10. Logging & Observability/03. Request Context and Correlation IDs/` | contextvars, propagation (`01`–`02`) |
| 76 | `10. Logging & Observability/04. FastAPI Logging Middleware/` | Request logging (`01`) |
| 77 | `10. Logging & Observability/05. Flask Logging/` | before/after request logs (`01`) |
| 78 | `10. Logging & Observability/06. Django Logging/` | LOGGING config (`01`–`02`) |
| 79 | `10. Logging & Observability/07. Health and Readiness Probes/` | K8s probes, deep health (`01`–`02`) |
| 80 | `10. Logging & Observability/08. Metrics with Prometheus/` | Counters, /metrics (`01`–`02`) |
| 81 | `10. Logging & Observability/09. Error Tracking/` | Sentry overview (`01`–`02`) |
| 82 | `10. Logging & Observability/10. Distributed Tracing/` | OpenTelemetry intro (`01`–`02`) |
| 83 | `10. Logging & Observability/11. Observability Capstone/` | Logs + health + metrics (`01`) |

## Quick commands

**SQLite** (no setup):
```bash
cd "01. Databases/01. SQLite"
python 01_sqlite_intro.py
```

**SQLAlchemy** (no server):
```bash
cd "01. Databases/04. SQLAlchemy"
python 01_engine_and_text.py
```

**Alembic** (SQLite file in folder):
```bash
cd "01. Databases/07. Alembic"
python 01_upgrade_initial.py
python 02_orm_crud.py
```

Copy `config.example.env` to repo root `.env` for MySQL, PostgreSQL, MongoDB, Redis, and RabbitMQ.

**Networking** (UDP/WebSocket — no extra services):
```bash
cd "02. Networking/03. UDP Programming"
python 02_udp_server.py   # terminal 1
python 03_udp_client.py   # terminal 2
```

**GraphQL**:
```bash
cd "02. Networking/05. GraphQL"
python 01_schema_and_types.py
uvicorn 02_graphql_server:app --port 8002
# Playground: http://127.0.0.1:8002/graphql
```

**gRPC**:
```bash
cd "02. Networking/07. gRPC"
python 01_generate_stubs.py
python 02_grpc_server.py
```

**Flask**:
```bash
cd "03. Flask/01. Lessons"
python 01_flask_concepts.py
python 03_hello.py
```

Optional extras for some lessons: `pip install flask-wtf flask-mail`

**FastAPI**:
```bash
cd "05. FastAPI/01. Lessons"
python 01_fastapi_concepts.py
uvicorn 02_hello:app --reload --port 8000
```

Optional extras for some lessons: `pip install jinja2 python-multipart "pydantic[email]" motor strawberry-graphql`

**Django**:
```bash
cd "04. Django/01. Lessons"
python 01_django_basics.py
python 08_url_mapping.py
# Open http://127.0.0.1:8001/users/42/
```

MySQL / PostgreSQL / MongoDB / Redis / RabbitMQ lessons need the matching service running and `.env` configured.

**Security** (mostly stdlib; some lessons need extra packages):
```bash
cd "06. Security/01. Passwords and Hashing"
python 01_password_hashing.py
python 02_bcrypt_hashes.py

cd "../04. Authentication"
python 02_jwt_basics.py

cd "../14. Security Capstone"
uvicorn 01_secure_notes_api:app --port 8012
# curl -H "X-API-Key: demo-key" http://127.0.0.1:8012/notes
```

Optional security extras: `pip install bcrypt pyjwt cryptography bandit pip-audit email-validator`

**Testing** (pytest-based; complements `01. Python Fundamentals/13. Unit Testing/`):
```bash
cd "07. Testing/03. Unit Testing Services"
pytest 01_test_notes_service.py -v

cd "../07. FastAPI Testing"
pytest 01_test_fastapi_client.py -v

cd "../14. Testing Capstone"
pytest test_notes_api.py -v
```

Install test extras: `pip install pytest pytest-cov pytest-asyncio`

**Deployment & DevOps**:
```bash
cd "08. Deployment & DevOps/01. Twelve-Factor and Environment"
python 03_pydantic_settings.py

cd "../03. Docker Basics"
python 01_build_and_run.py
# docker build -t backend-lesson-api:latest .
```

**Background jobs** (Redis required for RQ/Celery lessons):
```bash
cd "09. Background Jobs & Serverless Functions/03. RQ with Redis"
python 02_rq_inline_demo.py
python 01_enqueue_job.py
# rq worker --url redis://localhost:6379/0

cd "../08. AWS Lambda Basics"
python 01_lambda_handler.py
```

**Logging & Observability**:
```bash
cd "10. Logging & Observability/01. Python Logging Basics"
python 01_logging_basics.py

cd "../11. Observability Capstone"
uvicorn app:app --port 8024
```

Optional extras: `pip install pydantic-settings gunicorn waitress rq celery apscheduler prometheus-client mangum`
