# 03 — Gunicorn with Uvicorn workers (ASGI)
# Run: python 03_gunicorn_uvicorn_workers.py

if __name__ == "__main__":
    print("Install: pip install gunicorn uvicorn")
    print("\nRun FastAPI with Gunicorn + Uvicorn workers:")
    print("  gunicorn main:app -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000")
    print("\nFlags:")
    print("  -w 4          worker processes (often 2*CPU+1)")
    print("  -b 0.0.0.0:8000  bind address")
    print("  --timeout 60  kill slow workers")
    print("  --graceful-timeout 30  drain connections on reload")
