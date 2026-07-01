# 04 — GraphQL mutations
# Run: uvicorn 04_graphql_mutations:app --port 8003
# Then: python 04_graphql_mutation_client.py
# Install: pip install strawberry-graphql uvicorn

try:
    import strawberry
    from strawberry.asgi import GraphQL
except ImportError:
    print("Install: pip install strawberry-graphql")
    raise SystemExit(1)

_notes: list[dict] = []
_next_id = 1


@strawberry.type
class Note:
    id: int
    title: str


@strawberry.type
class Query:
    @strawberry.field
    def notes(self) -> list[Note]:
        return [Note(id=n["id"], title=n["title"]) for n in _notes]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_note(self, title: str) -> Note:
        global _next_id
        note = {"id": _next_id, "title": title}
        _notes.append(note)
        _next_id += 1
        return Note(id=note["id"], title=note["title"])


schema = strawberry.Schema(query=Query, mutation=Mutation)
app = GraphQL(schema)
