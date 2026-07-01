# 06 — Admin interface
# Run: python 06_admin_interface.py
# Open: http://127.0.0.1:8001/admin/
# First time: python 06_admin_interface.py createsuperuser  (in another terminal while server runs, or run:
#   set DJANGO_SETTINGS_MODULE - actually use manage pattern)
#
# Create superuser before first run:
#   python -c "from importlib import import_module; import sys; sys.argv=['x','createsuperuser','--noinput']; ..." 
# Simpler: visit admin after running - Django will prompt on first migrate.
#
# Easiest: run server, then in NEW terminal from same folder:
#   python 06_admin_interface.py --createsuperuser
# We'll add createsuperuser support in __main__

import sys

from django.contrib import admin
from django.db import models
from django.urls import path

from lesson_support import configure, create_tables, migrate, runserver


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        app_label = "__main__"

    def __str__(self):
        return self.name


admin.site.register(Product)

urlpatterns = [
    path("admin/", admin.site.urls),
]


if __name__ == "__main__":
    configure(lesson_id="06", urlpatterns=urlpatterns, with_admin=True, with_messages=True)
    migrate()
    create_tables(Product)
    if "--createsuperuser" in sys.argv:
        from django.core.management import call_command

        call_command("createsuperuser")
    else:
        print("Admin at http://127.0.0.1:8001/admin/")
        print("Create login (once): python 06_admin_interface.py --createsuperuser")
        runserver()
