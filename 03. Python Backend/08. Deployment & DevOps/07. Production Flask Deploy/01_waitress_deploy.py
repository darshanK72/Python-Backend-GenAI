# 01 — Deploy Flask with Waitress (Windows-friendly WSGI)
# Run: python 01_waitress_deploy.py
# Install: pip install waitress

try:
    from waitress import serve
except ImportError:
    print("Install: pip install waitress")
    raise SystemExit(1)

from app import app

if __name__ == "__main__":
    print("Serving Flask on http://127.0.0.1:5001")
    print("Health: http://127.0.0.1:5001/health")
    serve(app, host="127.0.0.1", port=5001, threads=4)
