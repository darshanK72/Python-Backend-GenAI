# 04 — Creating a project (runnable hello + structure notes)
# Run: python 04_creating_project.py
# Open: http://127.0.0.1:8001/
#
# A real Django project also has:
#   manage.py, mysite/settings.py, mysite/urls.py, myapp/models.py, views.py
# See capstone: ../01. Todo Project/

from django.http import HttpResponse
from django.urls import path

from lesson_support import configure, runserver


def home(request):
    return HttpResponse(
        "<h1>Lesson 04 — Django project</h1>"
        "<p>This single file runs a minimal site. The Todo Project shows a full layout.</p>"
    )


urlpatterns = [path("", home)]


if __name__ == "__main__":
    configure(lesson_id="04", urlpatterns=urlpatterns)
    runserver()
