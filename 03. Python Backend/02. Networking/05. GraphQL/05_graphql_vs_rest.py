# 05 — GraphQL vs REST (same resource, two styles)
# Run: python 05_graphql_vs_rest.py
# Install: pip install strawberry-graphql

try:
    import strawberry
except ImportError:
    print("Install: pip install strawberry-graphql")
    raise SystemExit(1)


@strawberry.type
class Book:
    id: int
    title: str
    author: str


BOOKS = [
    Book(id=1, title="Clean Code", author="Robert Martin"),
    Book(id=2, title="Fluent Python", author="Luciano Ramalho"),
]


@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return BOOKS

    @strawberry.field
    def book(self, id: int) -> Book | None:
        return next((b for b in BOOKS if b.id == id), None)


schema = strawberry.Schema(query=Query)

if __name__ == "__main__":
    print("GraphQL runs over HTTP POST with a query body.")
    print("Client asks for only the fields it needs.\n")

    all_books = schema.execute_sync("{ books { title } }")
    print("All titles:", all_books.data)

    one_book = schema.execute_sync("{ book(id: 2) { title author } }")
    print("One book:", one_book.data)
