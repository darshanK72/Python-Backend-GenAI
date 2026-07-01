# 01 — GraphQL schema and types (in-process query)
# Run: python 01_schema_and_types.py
# Install: pip install strawberry-graphql

try:
    import strawberry
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

if __name__ == "__main__":
    result = schema.execute_sync('{ hello(name: "Learner") }')
    print("Query result:", result.data)

    books = schema.execute_sync("{ books { title author } }")
    print("Books:", books.data)
