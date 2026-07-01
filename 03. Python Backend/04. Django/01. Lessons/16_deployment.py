# 16 — Deployment (read-only)
# Run: python 16_deployment.py

print("""
Development (lessons):
  python 08_url_mapping.py

Production:
  pip install gunicorn
  gunicorn --bind 0.0.0.0:8000 04_creating_project:application
  # For full projects, point gunicorn at mysite.wsgi:application

On Windows:
  pip install waitress
  waitress-serve --port=8000 module:app

Always:
  - DEBUG = False
  - Strong SECRET_KEY from environment
  - HTTPS via Nginx/Caddy reverse proxy
  - python manage.py collectstatic

Capstone: ../01. Todo Project/
""")
