# 01 — HTTPS and CORS overview
# Run: python 01_cors_and_https.py

if __name__ == "__main__":
    print("HTTPS encrypts traffic between client and server (TLS certificate).")
    print("CORS is a browser rule: your API must allow the frontend origin.\n")
    print("FastAPI:")
    print("  from fastapi.middleware.cors import CORSMiddleware")
    print("Django:")
    print("  pip install django-cors-headers")
    print("Flask:")
    print("  pip install flask-cors")
    print("\nProduction:")
    print("  - DEBUG=False")
    print("  - Strong SECRET_KEY")
    print("  - Restrict ALLOWED_HOSTS / trusted origins")
