# 19 — Caching
# Run: python 19_caching.py
# /slow/  — first request ~1s, then fast for 60s
# /counter/ — increments cached hit count

import time

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.urls import path
from django.views.decorators.cache import cache_page

from lesson_support import configure, runserver


@cache_page(60)
def slow_page(request):
    time.sleep(1)
    return HttpResponse("Rendered after 1 second (cached for 60s with @cache_page).")


def counter(request):
    count = cache.get("hits", 0) + 1
    cache.set("hits", count, 300)
    return JsonResponse({"hit_count": count})


urlpatterns = [
    path("slow/", slow_page),
    path("counter/", counter),
]


if __name__ == "__main__":
    configure(lesson_id="19", urlpatterns=urlpatterns, with_cache=True)
    runserver()
