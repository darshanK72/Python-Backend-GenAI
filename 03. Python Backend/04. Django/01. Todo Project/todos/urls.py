from django.urls import path
from . import views

urlpatterns = [
    path("api/todos/", views.todo_list),
    path("api/todos/create/", views.todo_create),
]
