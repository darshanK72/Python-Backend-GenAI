# 01 — Django concepts (read and run as reference)
# Run: python 01_django_concepts.py
#
# Full project: ../01. Todo Project/
# Setup:
#   cd "../01. Todo Project"
#   pip install django
#   python manage.py migrate
#   python manage.py createsuperuser
#   python manage.py runserver

concepts = """
Django building blocks:
  Project  = todo_site/     (settings, root urls)
  App      = todos/         (models, views, urls)
  Model    = database table (models.py)
  View     = request handler (views.py)
  URLconf  = route to view (urls.py)
  Admin    = built-in UI (admin.py)

Typical commands:
  python manage.py startapp myapp
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
"""

print(concepts)
