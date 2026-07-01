# 05 — Apps life cycle (migrate + ORM in one runnable script)
# Run: python 05_apps_lifecycle.py
# Open: http://127.0.0.1:8001/items/
# POST {"name": "Notebook"}

import json

from django.db import models
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from lesson_support import configure, create_tables, migrate, runserver


class Item(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "__main__"


@csrf_exempt
@require_http_methods(["GET", "POST"])
def items(request):
    if request.method == "GET":
        return JsonResponse({"items": list(Item.objects.values("id", "name"))})
    data = json.loads(request.body.decode() or "{}")
    item = Item.objects.create(name=data.get("name", "item"))
    return JsonResponse({"id": item.id, "name": item.name}, status=201)


urlpatterns = [path("items/", items)]


if __name__ == "__main__":
    configure(lesson_id="05", urlpatterns=urlpatterns)
    migrate()  # django.contrib tables (sessions/auth when needed)
    create_tables(Item)
    print("Lifecycle demo: migrate() + create_tables() + runserver()")
    runserver()
