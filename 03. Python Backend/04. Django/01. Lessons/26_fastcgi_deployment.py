# 26 — FastCGI recap + capstone pointer
# Run: python 26_fastcgi_deployment.py

print("""
FastCGI was used on older shared hosts. Modern Django uses WSGI (Gunicorn/Waitress).

Capstone project (full layout with admin + API):
  cd "../01. Todo Project"
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver

  Admin:  http://127.0.0.1:8000/admin/
  API:    http://127.0.0.1:8000/api/todos/
""")
