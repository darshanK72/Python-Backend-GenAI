# 02 — Environment setup (read-only)
# Run: python 02_environment.py
#
# Topics: venv, pip install flask, verify installation

import sys


def check_flask():
    try:
        import flask

        return flask.__version__
    except ImportError:
        return None


if __name__ == "__main__":
    print("Python:", sys.version.split()[0])
    version = check_flask()
    if version:
        print(f"Flask {version} is installed.")
        print("Next: python 03_hello.py")
    else:
        print("Flask not found. From repo root with venv active:")
        print("  pip install -r requirements.txt")
