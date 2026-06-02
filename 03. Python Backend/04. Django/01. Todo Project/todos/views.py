from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Todo


@require_http_methods(["GET"])
def todo_list(request):
    items = list(Todo.objects.values("id", "title", "done", "created_at"))
    return JsonResponse({"todos": items})


@require_http_methods(["POST"])
def todo_create(request):
    import json
    data = json.loads(request.body.decode() or "{}")
    title = data.get("title", "").strip()
    if not title:
        return JsonResponse({"error": "title required"}, status=400)
    todo = Todo.objects.create(title=title)
    return JsonResponse(
        {"id": todo.id, "title": todo.title, "done": todo.done},
        status=201,
    )
