# 09 — Template system
# Run: python 09_templates.py
# Open: http://127.0.0.1:8001/greeting/

from django.shortcuts import render
from django.urls import path

from lesson_support import configure, runserver


def greeting(request):
    return render(
        request,
        "09_greeting.html",
        {
            "title": "Django Templates",
            "user": "Learner",
            "tags": ["python", "django", "jinja2"],
        },
    )


urlpatterns = [
    path("greeting/", greeting),
]


if __name__ == "__main__":
    configure(lesson_id="09", urlpatterns=urlpatterns, with_messages=True)
    runserver()
