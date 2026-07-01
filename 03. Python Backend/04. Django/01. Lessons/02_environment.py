# 02 — Environment setup (read-only)
# Run: python 02_environment.py

import sys


def check_django():
    try:
        import django

        return django.get_version()
    except ImportError:
        return None


if __name__ == "__main__":
    print("Python:", sys.version.split()[0])
    version = check_django()
    if version:
        print(f"Django {version} is installed.")
        print("Next: python 03_overview_mvt.py")
    else:
        print("Django not found. From repo root with venv active:")
        print("  pip install -r requirements.txt")
