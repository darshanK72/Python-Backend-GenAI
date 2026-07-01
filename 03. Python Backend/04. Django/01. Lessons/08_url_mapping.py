# 08 — URL mapping
# Run: python 08_url_mapping.py
# Try: http://127.0.0.1:8001/users/42/

from django.http import JsonResponse
from django.urls import path

from lesson_support import configure, runserver


def home(request):
    return JsonResponse({"try": ["/users/42/", "/posts/2024/django-intro/"]})


def user_profile(request, user_id: int):
    return JsonResponse({"user_id": user_id})


def blog_post(request, year: int, slug: str):
    return JsonResponse({"year": year, "slug": slug})


urlpatterns = [
    path("", home),
    path("users/<int:user_id>/", user_profile),
    path("posts/<int:year>/<slug:slug>/", blog_post),
]


if __name__ == "__main__":
    configure(lesson_id="08", urlpatterns=urlpatterns)
    runserver()
