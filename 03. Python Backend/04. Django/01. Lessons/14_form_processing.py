# 14 — Form processing
# Run: python 14_form_processing.py
# Open: http://127.0.0.1:8001/contact/

from django import forms
from django.shortcuts import render
from django.urls import path

from lesson_support import configure, runserver


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")


def contact(request):
    submitted = False
    name = ""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            submitted = True
            name = form.cleaned_data["name"]
    else:
        form = ContactForm()
    return render(
        request,
        "14_contact.html",
        {"form": form, "submitted": submitted, "name": name},
    )


urlpatterns = [
    path("contact/", contact),
]


if __name__ == "__main__":
    configure(lesson_id="14", urlpatterns=urlpatterns, with_messages=True)
    runserver()
