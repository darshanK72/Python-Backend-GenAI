# 04 — GraphQL mutation client
# Run: python 04_graphql_mutation_client.py
# Server: uvicorn 04_graphql_mutations:app --port 8003

import requests

URL = "http://127.0.0.1:8003/graphql"

create_mutation = """
mutation Add($title: String!) {
  addNote(title: $title) {
    id
    title
  }
}
"""

list_query = "{ notes { id title } }"

if __name__ == "__main__":
    r = requests.post(
        URL,
        json={"query": create_mutation, "variables": {"title": "Learn GraphQL"}},
        timeout=10,
    )
    r.raise_for_status()
    print("created:", r.json())

    r2 = requests.post(URL, json={"query": list_query}, timeout=10)
    r2.raise_for_status()
    print("notes:", r2.json())
