# 01 — Role-based access control (RBAC)
# Run: python 01_rbac_roles.py

from enum import Enum


class Role(str, Enum):
    VIEWER = "viewer"
    EDITOR = "editor"
    ADMIN = "admin"


ROLE_PERMISSIONS = {
    Role.VIEWER: {"read"},
    Role.EDITOR: {"read", "write"},
    Role.ADMIN: {"read", "write", "delete", "manage_users"},
}


def can(user_role: Role, action: str) -> bool:
    return action in ROLE_PERMISSIONS.get(user_role, set())


if __name__ == "__main__":
    for role in Role:
        print(f"{role.value}: delete allowed = {can(role, 'delete')}")
