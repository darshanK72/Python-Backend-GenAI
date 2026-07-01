# 23 — GraphQL (Strawberry)
# Run: uvicorn 23_graphql:app --reload --port 8000
# Playground: http://127.0.0.1:8000/graphql
# Install: pip install strawberry-graphql
#
# Example query:
#   { hello(name: "FastAPI") }
#   { books { title author } }

from fastapi import FastAPI

try:
    import strawberry
    from strawberry.fastapi import GraphQLRouter
except ImportError:
    strawberry = None  # type: ignore[assignment]
    GraphQLRouter = None  # type: ignore[assignment]

app = FastAPI(title="Lesson 23 — GraphQL")

if strawberry and GraphQLRouter:

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
    app.include_router(GraphQLRouter(schema), prefix="/graphql")
else:

    @app.get("/graphql")
    def graphql_unavailable():
        return {
            "error": "Install strawberry-graphql: pip install strawberry-graphql"
        }
