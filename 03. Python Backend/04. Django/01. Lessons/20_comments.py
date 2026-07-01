# 20 — Comments
# Run: python 20_comments.py
# Open: http://127.0.0.1:8001/articles/hello-world/comments/

from django import forms
from django.db import models
from django.shortcuts import redirect, render
from django.urls import path

from lesson_support import configure, create_tables, migrate, runserver


class Comment(models.Model):
    article_slug = models.SlugField(max_length=80)
    author_name = models.CharField(max_length=80)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "__main__"
        ordering = ["-created_at"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "text"]


def article_comments(request, slug: str):
    comments = Comment.objects.filter(article_slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_slug = slug
            comment.save()
            return redirect("article_comments", slug=slug)
    else:
        form = CommentForm()
    return render(
        request,
        "20_comments.html",
        {"slug": slug, "comments": comments, "form": form},
    )


urlpatterns = [
    path("articles/<slug:slug>/comments/", article_comments, name="article_comments"),
]


if __name__ == "__main__":
    configure(lesson_id="20", urlpatterns=urlpatterns, with_messages=True)
    migrate()
    create_tables(Comment)
    runserver()
