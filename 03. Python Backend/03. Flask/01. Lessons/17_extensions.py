# 17 — Flask extensions (read-only)
# Run: python 17_extensions.py
#
# Flask stays small; extensions add features. Common ones:

EXTENSIONS = {
    "Flask-SQLAlchemy": "ORM integration",
    "Flask-Migrate": "Alembic database migrations",
    "Flask-WTF": "WTForms + CSRF protection",
    "Flask-Login": "User session management",
    "Flask-Mail": "Send email",
    "Flask-CORS": "Cross-origin headers for APIs",
    "Flask-RESTful": "REST API resources (legacy; prefer plain routes or FastAPI)",
}

if __name__ == "__main__":
    print("Popular Flask extensions:\n")
    for name, desc in EXTENSIONS.items():
        print(f"  {name:20} — {desc}")
    print("\nNext lessons: 18_mail.py, 19_wtf_forms.py, 22_sqlalchemy.py")
