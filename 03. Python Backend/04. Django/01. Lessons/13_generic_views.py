# 13 — Generic views
# Run: python 13_generic_views.py
# Open: http://127.0.0.1:8001/products/
# Seed: POST /api/products/  {"name": "Notebook", "price": "120.00"}

import json

from django.db import models
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from lesson_support import configure, create_tables, migrate, runserver


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        app_label = "__main__"


class ProductListView(ListView):
    model = Product
    template_name = "13_product_list.html"


@csrf_exempt
@require_http_methods(["POST"])
def seed_product(request):
    data = json.loads(request.body.decode() or "{}")
    product = Product.objects.create(name=data["name"], price=data.get("price", "0"))
    return JsonResponse({"id": product.id, "name": product.name}, status=201)


urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("api/products/", seed_product),
]


if __name__ == "__main__":
    configure(lesson_id="13", urlpatterns=urlpatterns, with_messages=True)
    migrate()
    create_tables(Product)
    runserver()
