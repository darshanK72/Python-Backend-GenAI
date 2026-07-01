# 01 — Django LOGGING settings example
# Run: python 01_django_logging_config.py

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "loggers": {
        "django.request": {"handlers": ["console"], "level": "WARNING"},
        "myapp": {"handlers": ["console"], "level": "INFO"},
    },
}

if __name__ == "__main__":
    import json

    print("Django LOGGING dict (put in settings.py):\n")
    print(json.dumps(LOGGING_CONFIG, indent=2))
