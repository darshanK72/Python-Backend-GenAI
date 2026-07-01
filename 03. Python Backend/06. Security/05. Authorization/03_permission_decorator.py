# 03 — Permission decorator pattern
# Run: python 03_permission_decorator.py

from functools import wraps


def require_permission(permission: str):
    def decorator(func):
        @wraps(func)
        def wrapper(user: dict, *args, **kwargs):
            if permission not in user.get("permissions", []):
                return {"error": "forbidden"}, 403
            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@require_permission("delete")
def delete_note(user: dict, note_id: int):
    return {"deleted": note_id}, 200


if __name__ == "__main__":
    viewer = {"id": 1, "permissions": ["read"]}
    admin = {"id": 2, "permissions": ["read", "delete"]}
    print("Viewer delete:", delete_note(viewer, 5))
    print("Admin delete:", delete_note(admin, 5))
