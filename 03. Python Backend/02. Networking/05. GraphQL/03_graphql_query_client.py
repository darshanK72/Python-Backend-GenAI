# 03 — GraphQL HTTP client (requests)
# Run: python 03_graphql_query_client.py
# Start server first: uvicorn 02_graphql_server:app --port 8002

import requests

URL = "http://127.0.0.1:8002/graphql"

hello_query = """
query Hello($name: String!) {
  hello(name: $name)
}
"""

books_query = """
query {
  books {
    title
    author
  }
}
"""

if __name__ == "__main__":
    r1 = requests.post(
        URL,
        json={"query": hello_query, "variables": {"name": "Learner"}},
        timeout=10,
    )
    r1.raise_for_status()
    print("hello:", r1.json())

    r2 = requests.post(URL, json={"query": books_query}, timeout=10)
    r2.raise_for_status()
    print("books:", r2.json())
