# 02 — GraphQL server over HTTP (Strawberry ASGI)
# Run: uvicorn 02_graphql_server:app --port 8002
# Playground: http://127.0.0.1:8002/graphql
# Install: pip install strawberry-graphql uvicorn

try:
    import strawberry
    from strawberry.asgi import GraphQL
except ImportError:
    print("Install: pip install strawberry-graphql")
    raise SystemExit(1)


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str = "World") -> str:
        return f"Hello, {name}!"

    @strawberry.field
    def books(self) -> list[Book]:
        return [
            Book(title="Clean Code", author="Robert Martin"),
            Book(title="Fluent Python", author="Luciano Ramalho"),
        ]


schema = strawberry.Schema(query=Query)
app = GraphQL(schema)
