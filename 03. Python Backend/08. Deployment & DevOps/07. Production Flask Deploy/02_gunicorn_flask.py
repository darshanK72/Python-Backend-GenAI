# 02 — Gunicorn for Flask (Linux/macOS)
# Run: python 02_gunicorn_flask.py

if __name__ == "__main__":
    print("Linux/macOS production command:")
    print("  pip install gunicorn")
    print("  gunicorn -w 4 -b 127.0.0.1:5001 app:app")
    print("\nWindows: use Waitress instead of Gunicorn.")
