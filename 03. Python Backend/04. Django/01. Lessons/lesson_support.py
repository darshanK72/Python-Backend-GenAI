"""Bootstrap helper so each lesson file can run as: python NN_topic.py"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import django
from django.conf import settings

LESSONS_DIR = Path(__file__).resolve().parent
DB_DIR = LESSONS_DIR / "_db"
TEMPLATE_DIR = LESSONS_DIR / "_templates"
STATIC_DIR = LESSONS_DIR / "_static"


def configure(
    *,
    lesson_id: str,
    urlpatterns: list,
    middleware: list[str] | None = None,
    with_admin: bool = False,
    with_sessions: bool = False,
    with_messages: bool = False,
    email_console: bool = False,
    with_cache: bool = False,
    extra_settings: dict[str, Any] | None = None,
) -> None:
    if settings.configured:
        return

    DB_DIR.mkdir(exist_ok=True)

    installed = ["django.contrib.contenttypes"]
    if with_admin or with_sessions or with_messages:
        installed.append("django.contrib.auth")
    if with_admin:
        installed.extend(["django.contrib.admin", "django.contrib.staticfiles"])
    if with_sessions:
        installed.append("django.contrib.sessions")
    if with_messages:
        installed.append("django.contrib.messages")
    if "django.contrib.staticfiles" not in installed:
        installed.append("django.contrib.staticfiles")
    installed.append("__main__")

    default_middleware = [
        "django.middleware.security.SecurityMiddleware",
    ]
    if with_sessions:
        default_middleware.append("django.contrib.sessions.middleware.SessionMiddleware")
    default_middleware.extend(
        [
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
        ]
    )
    if with_admin or with_sessions:
        default_middleware.append("django.contrib.auth.middleware.AuthenticationMiddleware")
    if with_messages:
        default_middleware.append("django.contrib.messages.middleware.MessageMiddleware")
    if with_admin:
        default_middleware.append("django.middleware.clickjacking.XFrameOptionsMiddleware")
    if middleware:
        default_middleware.extend(middleware)

    cfg: dict[str, Any] = {
        "DEBUG": True,
        "SECRET_KEY": "django-lesson-dev-only",
        "ROOT_URLCONF": "__main__",
        "ALLOWED_HOSTS": ["127.0.0.1", "localhost"],
        "INSTALLED_APPS": installed,
        "MIDDLEWARE": default_middleware,
        "DATABASES": {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": DB_DIR / f"{lesson_id}.sqlite3",
            }
        },
        "TEMPLATES": [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [TEMPLATE_DIR],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            }
        ],
        "STATIC_URL": "/static/",
        "STATICFILES_DIRS": [STATIC_DIR],
        "USE_TZ": True,
    }
    if email_console:
        cfg["EMAIL_BACKEND"] = "django.core.mail.backends.console.EmailBackend"
    if with_cache:
        cfg["CACHES"] = {
            "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}
        }
    if extra_settings:
        cfg.update(extra_settings)

    settings.configure(**cfg)
    django.setup()

    import __main__

    __main__.urlpatterns = urlpatterns


def migrate() -> None:
    from django.core.management import call_command

    call_command("migrate", verbosity=0, interactive=False)


def create_tables(*models) -> None:
    """Create tables for lesson-defined models (no migrations folder needed)."""
    from django.db import connection

    with connection.schema_editor() as editor:
        for model in models:
            try:
                editor.create_model(model)
            except Exception:
                pass  # table already exists from a previous run


def runserver(port: int = 8001) -> None:
    from django.core.management import execute_from_command_line

    print(f"Server: http://127.0.0.1:{port}/  (Ctrl+C to stop)")
    execute_from_command_line([sys.argv[0], "runserver", f"127.0.0.1:{port}", "--noreload"])
