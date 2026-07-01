# 02 — Log Django 404/500 server errors
# Run: python 02_django_request_errors.py

if __name__ == "__main__":
    print("django.request logger captures 4xx/5xx responses.")
    print("Set LOGGING level WARNING for django.request in production.")
    print("Never return stack traces to clients — log server-side only.")
