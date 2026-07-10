"""Tests for POST/GET/DELETE /notes endpoints."""

from fastapi.testclient import TestClient


def test_authed_create_succeeds(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.post(
        "/notes",
        headers=auth_headers,
        json={"title": "First", "body": "Hello"},
    )
    assert response.status_code == 201
    payload = response.json()
    assert payload["title"] == "First"
    assert payload["body"] == "Hello"
    assert payload["id"] == 1
    assert "created_at" in payload


def test_unauthed_create_is_401(client: TestClient) -> None:
    response = client.post("/notes", json={"title": "Nope", "body": "Denied"})
    assert response.status_code == 401


def test_create_with_invalid_api_key_is_401(client: TestClient) -> None:
    response = client.post(
        "/notes",
        headers={"X-API-Key": "wrong-key"},
        json={"title": "Nope", "body": "Denied"},
    )
    assert response.status_code == 401


def test_create_empty_title_is_422(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.post(
        "/notes",
        headers=auth_headers,
        json={"title": "", "body": "Hello"},
    )
    assert response.status_code == 422


def test_create_missing_body_is_422(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.post(
        "/notes",
        headers=auth_headers,
        json={"title": "Title only"},
    )
    assert response.status_code == 422


def test_list_pagination_works(client: TestClient, auth_headers: dict[str, str]) -> None:
    for index in range(3):
        client.post(
            "/notes",
            headers=auth_headers,
            json={"title": f"Note {index}", "body": "Body"},
        )

    response = client.get("/notes", params={"limit": 2, "offset": 1})
    assert response.status_code == 200
    payload = response.json()
    assert payload["total"] == 3
    assert payload["limit"] == 2
    assert payload["offset"] == 1
    assert len(payload["items"]) == 2
    assert payload["items"][0]["title"] == "Note 1"


def test_list_defaults_to_limit_10(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json()["limit"] == 10
    assert response.json()["offset"] == 0


def test_list_rejects_limit_over_100(client: TestClient) -> None:
    response = client.get("/notes", params={"limit": 101})
    assert response.status_code == 422


def test_get_note_succeeds(client: TestClient, auth_headers: dict[str, str]) -> None:
    created = client.post(
        "/notes",
        headers=auth_headers,
        json={"title": "Read me", "body": "Content"},
    )
    note_id = created.json()["id"]

    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Read me"


def test_get_missing_is_404(client: TestClient) -> None:
    response = client.get("/notes/999")
    assert response.status_code == 404


def test_delete_works(client: TestClient, auth_headers: dict[str, str]) -> None:
    create = client.post(
        "/notes",
        headers=auth_headers,
        json={"title": "Delete me", "body": "Soon gone"},
    )
    note_id = create.json()["id"]

    delete = client.delete(f"/notes/{note_id}", headers=auth_headers)
    assert delete.status_code == 204

    get_after = client.get(f"/notes/{note_id}")
    assert get_after.status_code == 404


def test_unauthed_delete_is_401(client: TestClient, auth_headers: dict[str, str]) -> None:
    create = client.post(
        "/notes",
        headers=auth_headers,
        json={"title": "Protected", "body": "Cannot delete without key"},
    )
    note_id = create.json()["id"]

    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 401


def test_delete_missing_note_is_404(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.delete("/notes/999", headers=auth_headers)
    assert response.status_code == 404


def test_openapi_documents_note_schemas(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    components = schema["components"]["schemas"]

    assert "/notes" in schema["paths"]
    assert "Note" in components
    assert "NoteCreate" in components
    assert "NoteListResponse" in components
