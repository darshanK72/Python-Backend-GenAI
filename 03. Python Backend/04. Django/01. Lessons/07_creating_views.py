# 07 — Creating views
# Run: python 07_creating_views.py
# Open: http://127.0.0.1:8001/

from django.http import HttpResponse
from django.urls import path

from lesson_support import configure, runserver


def hello(request):
    return HttpResponse("<h1>Hello, Django!</h1><p>This is a function-based view.</p>")


urlpatterns = [
    path("", hello),
]


if __name__ == "__main__":
    configure(lesson_id="07", urlpatterns=urlpatterns)
    runserver()
