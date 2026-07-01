# 17 — Cookies
# Run: python 17_cookies.py
# 1. http://127.0.0.1:8001/set-cookie/
# 2. http://127.0.0.1:8001/read-cookie/

from django.http import HttpResponse, JsonResponse
from django.urls import path

from lesson_support import configure, runserver


def set_cookie(request):
    response = HttpResponse("Cookie set. Now open /read-cookie/")
    response.set_cookie("visits", "1", max_age=3600)
    return response


def read_cookie(request):
    return JsonResponse({"visits_cookie": request.COOKIES.get("visits", "not set")})


urlpatterns = [
    path("set-cookie/", set_cookie),
    path("read-cookie/", read_cookie),
]


if __name__ == "__main__":
    configure(lesson_id="17", urlpatterns=urlpatterns)
    runserver()
