# 03 — Django/FastAPI production settings snapshot
# Run: python 03_framework_prod_settings.py

DJANGO_SETTINGS = {
    "DEBUG": False,
    "SECRET_KEY": "from-env-only",
    "ALLOWED_HOSTS": ["api.example.com"],
    "SECURE_SSL_REDIRECT": True,
    "SESSION_COOKIE_SECURE": True,
    "CSRF_COOKIE_SECURE": True,
}

FASTAPI_NOTES = [
    "Set docs_url=None in production if you do not want public OpenAPI",
    "Use CORSMiddleware with explicit allow_origins",
    "Validate all input with Pydantic models",
    "Use Depends() for auth on protected routes",
]

if __name__ == "__main__":
    print("Django production flags:")
    for k, v in DJANGO_SETTINGS.items():
        print(f"  {k} = {v}")
    print("\nFastAPI reminders:")
    for note in FASTAPI_NOTES:
        print(f"  - {note}")
