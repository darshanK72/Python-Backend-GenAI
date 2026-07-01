# 24 — Middleware
# Run: python 24_middleware.py
# Open: http://127.0.0.1:8001/info/
# Check response header X-Lesson in browser dev tools (Network tab)

from django.http import JsonResponse
from django.urls import path

from lesson_support import configure, runserver


class LessonHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Lesson"] = "django-lesson-24"
        return response


def request_info(request):
    return JsonResponse({
        "path": request.path,
        "method": request.method,
        "note": "Inspect response headers for X-Lesson",
    })


urlpatterns = [
    path("info/", request_info),
]


if __name__ == "__main__":
    configure(
        lesson_id="24",
        urlpatterns=urlpatterns,
        middleware=["__main__.LessonHeaderMiddleware"],
    )
    runserver()
