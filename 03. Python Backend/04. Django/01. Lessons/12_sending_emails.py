# 12 — Sending emails
# Run: python 12_sending_emails.py
# Open: http://127.0.0.1:8001/send-email/
# Email body prints in this terminal (console backend).

from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import path

from lesson_support import configure, runserver


def send_demo_email(request):
    send_mail(
        subject="Django lesson email",
        message="If you see this in the terminal, email sending works.",
        from_email=None,
        recipient_list=["learner@example.com"],
    )
    return HttpResponse("Email sent — check the terminal running this script.")


urlpatterns = [
    path("send-email/", send_demo_email),
]


if __name__ == "__main__":
    configure(lesson_id="12", urlpatterns=urlpatterns, email_console=True)
    runserver()
