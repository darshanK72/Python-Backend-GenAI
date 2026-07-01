# 02 — Insecure Direct Object Reference (IDOR) prevention
# Run: python 02_idor_prevention.py

# BAD: GET /notes/5 returns any note if you only check note id
# GOOD: also check note.owner_id == current_user.id

NOTES = {
    1: {"id": 1, "owner_id": 10, "title": "Alice private note"},
    2: {"id": 2, "owner_id": 20, "title": "Bob private note"},
}


def get_note_unsafe(note_id: int):
    return NOTES.get(note_id)


def get_note_safe(note_id: int, current_user_id: int):
    note = NOTES.get(note_id)
    if not note:
        return None
    if note["owner_id"] != current_user_id:
        return "FORBIDDEN"
    return note


if __name__ == "__main__":
    print("Unsafe (user 10 reads note 2):", get_note_unsafe(2))
    print("Safe (user 10 reads note 2):", get_note_safe(2, current_user_id=10))
    print("Safe (user 20 reads note 2):", get_note_safe(2, current_user_id=20))
