# 18 — Sessions
# Run: python 18_sessions.py
# 1. http://127.0.0.1:8001/login/
# 2. http://127.0.0.1:8001/profile/

from django.http import JsonResponse
from django.urls import path

from lesson_support import configure, migrate, runserver


def login(request):
    request.session["username"] = "demo"
    return JsonResponse({"message": "Session set", "username": "demo"})


def profile(request):
    return JsonResponse({"username": request.session.get("username", "anonymous")})


def logout(request):
    request.session.flush()
    return JsonResponse({"message": "Logged out"})


urlpatterns = [
    path("login/", login),
    path("profile/", profile),
    path("logout/", logout),
]


if __name__ == "__main__":
    configure(lesson_id="18", urlpatterns=urlpatterns, with_sessions=True)
    migrate()
    runserver()
