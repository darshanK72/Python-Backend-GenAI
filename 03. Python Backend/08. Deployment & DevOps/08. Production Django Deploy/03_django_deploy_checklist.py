# 03 — Django deploy checklist
# Run: python 03_django_deploy_checklist.py

STEPS = [
    "python manage.py collectstatic --noinput",
    "python manage.py migrate --noinput",
    "Set DEBUG=False and strong SECRET_KEY",
    "Configure DATABASE_URL for production DB",
    "Run Gunicorn/Uvicorn behind HTTPS proxy",
]

if __name__ == "__main__":
    print("Django release steps:\n")
    for i, step in enumerate(STEPS, 1):
        print(f"  {i}. {step}")
