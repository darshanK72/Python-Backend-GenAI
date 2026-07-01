# 15 — File uploading
# Run: python 15_file_uploading.py
# Open: http://127.0.0.1:8001/upload/

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from lesson_support import configure, runserver


def upload_file(request):
    if request.method == "POST" and request.FILES.get("document"):
        uploaded = request.FILES["document"]
        return HttpResponse(f"Uploaded: {uploaded.name} ({uploaded.size} bytes)")
    return render(request, "15_upload.html")


urlpatterns = [
    path("upload/", upload_file),
]


if __name__ == "__main__":
    configure(lesson_id="15", urlpatterns=urlpatterns, with_messages=True)
    runserver()
