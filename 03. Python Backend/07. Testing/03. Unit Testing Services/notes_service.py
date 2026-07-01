# Code under test — notes service (no HTTP layer)


class NotesService:
    def __init__(self):
        self._notes: dict[int, dict] = {}
        self._next_id = 1

    def create(self, title: str, body: str = "") -> dict:
        if not title.strip():
            raise ValueError("title required")
        note = {"id": self._next_id, "title": title.strip(), "body": body}
        self._notes[self._next_id] = note
        self._next_id += 1
        return note

    def list_all(self) -> list[dict]:
        return list(self._notes.values())

    def get(self, note_id: int) -> dict | None:
        return self._notes.get(note_id)
