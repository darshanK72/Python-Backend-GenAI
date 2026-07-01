# 25 — Static files
# Run: python 25_static_files.py
# Open: http://127.0.0.1:8001/static/style.css

from django.http import JsonResponse
from django.urls import path

from lesson_support import configure, runserver


def home(request):
    return JsonResponse({
        "static_css": "/static/style.css",
        "message": "Open the URL above in your browser",
    })


urlpatterns = [
    path("", home),
]


if __name__ == "__main__":
    configure(lesson_id="25", urlpatterns=urlpatterns)
    runserver()
