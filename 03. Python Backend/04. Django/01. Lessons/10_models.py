# 10 — Models
# Run: python 10_models.py
# Open: http://127.0.0.1:8001/products/
# POST http://127.0.0.1:8001/products/  {"name": "Pen", "price": "25.00"}

import json

from django.db import models
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from lesson_support import configure, create_tables, migrate, runserver


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        app_label = "__main__"

    def __str__(self):
        return self.name


@require_http_methods(["GET", "POST"])
@csrf_exempt
def products(request):
    if request.method == "GET":
        rows = list(Product.objects.values("id", "name", "price"))
        return JsonResponse({"products": rows})

    data = json.loads(request.body.decode() or "{}")
    name = str(data.get("name", "")).strip()
    price = data.get("price", "0")
    if not name:
        return JsonResponse({"error": "name required"}, status=400)
    product = Product.objects.create(name=name, price=price)
    return JsonResponse({"id": product.id, "name": product.name, "price": str(product.price)}, status=201)


urlpatterns = [
    path("products/", products),
]


if __name__ == "__main__":
    configure(lesson_id="10", urlpatterns=urlpatterns)
    migrate()
    create_tables(Product)
    runserver()
