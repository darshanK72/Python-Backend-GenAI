# 22 — AJAX
# Run: python 22_ajax.py
# Open: http://127.0.0.1:8001/  — click "Load greeting"

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path

from lesson_support import configure, runserver


def ajax_page(request):
    return render(request, "22_ajax.html")


def ajax_greeting(request):
    return JsonResponse({"message": "Hello from Django JSON API!"})


urlpatterns = [
    path("", ajax_page),
    path("api/greeting/", ajax_greeting),
]


if __name__ == "__main__":
    configure(lesson_id="22", urlpatterns=urlpatterns, with_messages=True)
    runserver()
