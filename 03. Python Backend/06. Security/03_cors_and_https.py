# 03 — CORS and HTTPS (overview)
# Run: python 03_cors_and_https.py

print("HTTPS encrypts traffic between browser and server (TLS certificate)")
print("CORS = browser security; API must allow frontend origin")
print("FastAPI: from fastapi.middleware.cors import CORSMiddleware")
print("Django: django-cors-headers package for DRF/frontends")
print("Production: set DEBUG=False, strong SECRET_KEY, restrict ALLOWED_HOSTS")
