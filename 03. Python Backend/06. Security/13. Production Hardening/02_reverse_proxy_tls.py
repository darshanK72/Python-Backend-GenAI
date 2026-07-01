# 02 — Reverse proxy and TLS termination (overview)
# Run: python 02_reverse_proxy_tls.py

if __name__ == "__main__":
    print("Typical production stack:\n")
    print("  Internet -> Nginx/Caddy (TLS) -> Gunicorn/Uvicorn (app)")
    print("\nApp binds to 127.0.0.1 only; proxy handles:")
    print("  - TLS certificates (Let's Encrypt)")
    print("  - HSTS and security headers")
    print("  - Rate limiting and request size limits")
    print("\nUvicorn example:")
    print("  uvicorn main:app --host 127.0.0.1 --port 8000 --workers 4")
