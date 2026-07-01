# 01 — Manual test data factory
# Run: python 01_factory_pattern.py


def make_user(**overrides):
    user = {"id": 1, "username": "learner", "email": "learner@example.com", "role": "viewer"}
    user.update(overrides)
    return user


def make_note(**overrides):
    note = {"id": 1, "title": "Sample", "body": ""}
    note.update(overrides)
    return note


if __name__ == "__main__":
    admin = make_user(role="admin", username="admin1")
    draft = make_note(title="Draft note", body="content")
    print("User:", admin)
    print("Note:", draft)
