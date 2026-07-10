"""Integration tests for full CRUD cycle."""

from fastapi.testclient import TestClient


def test_create_list_get_delete_cycle(client: TestClient, auth_headers: dict[str, str]) -> None:
    create = client.post(
        "/notes",
        headers=auth_headers,
        json={"title": "Sprint retro", "body": "Discuss blockers"},
    )
    assert create.status_code == 201
    note_id = create.json()["id"]

    listed = client.get("/notes")
    assert listed.status_code == 200
    assert listed.json()["total"] == 1
    assert listed.json()["items"][0]["id"] == note_id

    fetched = client.get(f"/notes/{note_id}")
    assert fetched.status_code == 200
    assert fetched.json()["body"] == "Discuss blockers"

    deleted = client.delete(f"/notes/{note_id}", headers=auth_headers)
    assert deleted.status_code == 204

    missing = client.get(f"/notes/{note_id}")
    assert missing.status_code == 404


def test_pagination_across_multiple_pages(client: TestClient, auth_headers: dict[str, str]) -> None:
    for index in range(5):
        client.post(
            "/notes",
            headers=auth_headers,
            json={"title": f"Page note {index}", "body": "content"},
        )

    page_one = client.get("/notes", params={"limit": 2, "offset": 0}).json()
    page_two = client.get("/notes", params={"limit": 2, "offset": 2}).json()

    assert page_one["total"] == 5
    assert len(page_one["items"]) == 2
    assert len(page_two["items"]) == 2
    assert page_one["items"][0]["id"] != page_two["items"][0]["id"]
