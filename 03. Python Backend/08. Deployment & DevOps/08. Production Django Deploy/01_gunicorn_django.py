# 01 — Django production deployment overview
# Run: python 01_gunicorn_django.py

if __name__ == "__main__":
    print("Django production stack:\n")
    print("  1. collectstatic -> CDN or Nginx")
    print("  2. migrate on deploy")
    print("  3. gunicorn mysite.wsgi:application -w 4 -b 127.0.0.1:8001")
    print("  4. Nginx proxies to Gunicorn, serves /static/")
    print("\nSettings:")
    print("  DEBUG = False")
    print("  ALLOWED_HOSTS = ['api.example.com']")
    print("  SECRET_KEY from environment")
