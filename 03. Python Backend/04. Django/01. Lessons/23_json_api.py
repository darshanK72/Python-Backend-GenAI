# 23 — JSON API
# Run: python 23_json_api.py
# GET  http://127.0.0.1:8001/api/products/
# POST http://127.0.0.1:8001/api/products/  {"name": "Pen", "price": "20.00"}

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


@csrf_exempt
@require_http_methods(["GET", "POST"])
def product_api(request):
    if request.method == "GET":
        rows = list(Product.objects.values("id", "name", "price"))
        for row in rows:
            row["price"] = str(row["price"])
        return JsonResponse({"products": rows})

    data = json.loads(request.body.decode() or "{}")
    name = str(data.get("name", "")).strip()
    if not name:
        return JsonResponse({"error": "name required"}, status=400)
    product = Product.objects.create(name=name, price=data.get("price", "0"))
    return JsonResponse(
        {"id": product.id, "name": product.name, "price": str(product.price)},
        status=201,
    )


urlpatterns = [
    path("api/products/", product_api),
]


if __name__ == "__main__":
    configure(lesson_id="23", urlpatterns=urlpatterns)
    migrate()
    create_tables(Product)
    runserver()
