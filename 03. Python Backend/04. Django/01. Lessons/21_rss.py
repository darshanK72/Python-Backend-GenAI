# 21 — RSS feeds
# Run: python 21_rss.py
# Open: http://127.0.0.1:8001/books/feed/
# Seed: POST /api/books/  {"title": "Fluent Python", "author": "Luciano Ramalho"}

import json

from django.contrib.syndication.views import Feed
from django.db import models
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from lesson_support import configure, create_tables, migrate, runserver


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "__main__"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        app_label = "__main__"


class LatestBooksFeed(Feed):
    title = "Lesson books"
    link = "/books/feed/"
    description = "Latest books added in this lesson"

    def items(self):
        return Book.objects.order_by("-id")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return f"By {item.author.name}"


@csrf_exempt
@require_http_methods(["POST"])
def create_book(request):
    data = json.loads(request.body.decode() or "{}")
    author, _ = Author.objects.get_or_create(name=data.get("author", "Unknown"))
    book = Book.objects.create(title=data["title"], author=author)
    return JsonResponse({"id": book.id, "title": book.title, "author": author.name}, status=201)


urlpatterns = [
    path("books/feed/", LatestBooksFeed(), name="book_feed"),
    path("api/books/", create_book),
]


if __name__ == "__main__":
    configure(lesson_id="21", urlpatterns=urlpatterns)
    migrate()
    create_tables(Author, Book)
    runserver()
