# Django bootstrap for testing lessons

from pathlib import Path

import django
from django.conf import settings
from django.http import JsonResponse
from django.urls import path

DB_DIR = Path(__file__).resolve().parent / "_db"


def configure() -> None:
    if settings.configured:
        return
    DB_DIR.mkdir(exist_ok=True)
    settings.configure(
        DEBUG=True,
        SECRET_KEY="django-testing-lesson-only",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["testserver"],
        INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.staticfiles"],
        MIDDLEWARE=["django.middleware.common.CommonMiddleware"],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": DB_DIR / "test.sqlite3",
            }
        },
        USE_TZ=True,
    )
    django.setup()


def health(request):
    return JsonResponse({"status": "ok"})


def list_notes(request):
    return JsonResponse({"notes": []})


urlpatterns = [
    path("health/", health),
    path("notes/", list_notes),
]
