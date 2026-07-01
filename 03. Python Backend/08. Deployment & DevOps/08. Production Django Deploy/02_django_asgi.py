# 02 — Django ASGI with Uvicorn (async views, WebSockets)
# Run: python 02_django_asgi.py

if __name__ == "__main__":
    print("Django ASGI entry: mysite.asgi:application")
    print("Run:")
    print("  uvicorn mysite.asgi:application --host 127.0.0.1 --port 8001")
    print("\nUse when you need async views or Django Channels.")
