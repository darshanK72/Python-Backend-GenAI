# 01 — WSGI vs ASGI
# Run: python 01_wsgi_vs_asgi.py

if __name__ == "__main__":
    print("WSGI (sync, one request at a time per worker):")
    print("  Flask, Django (default), Waitress, Gunicorn sync workers")
    print("\nASGI (async-capable, WebSockets, SSE):")
    print("  FastAPI, Starlette, Django ASGI, Uvicorn, Hypercorn")
    print("\nRule of thumb:")
    print("  Flask/Django classic -> WSGI + Gunicorn/Waitress")
    print("  FastAPI/async APIs   -> ASGI + Uvicorn (or Gunicorn + UvicornWorker)")
