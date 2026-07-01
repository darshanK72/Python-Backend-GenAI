# 11 — Page redirection
# Run: python 11_page_redirection.py
# Try: http://127.0.0.1:8001/old-home/  -> redirects to /

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path, reverse

from lesson_support import configure, runserver


def home(request):
    return HttpResponse("<h1>Home</h1><p>Try /old-home/ or /go-home/</p>")


def old_home(request):
    return redirect("home")


def go_home(request):
    return redirect(reverse("home"))


urlpatterns = [
    path("", home, name="home"),
    path("old-home/", old_home),
    path("go-home/", go_home),
]


if __name__ == "__main__":
    configure(lesson_id="11", urlpatterns=urlpatterns)
    runserver()
