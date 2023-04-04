# test_api_citation.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_citation():
    # Given
    item_data = {
        "title": "Citation1",
        "content": "test citation1",
        "source": "...",
        "tags": ["action", "s-f"],
        "preference": 2
    }
    # When
    response = client.post("/api/v1/pins", json=item_data)

    # Then
    assert response.status_code == 200
    assert response.json()["title"] == "Citation1"
    assert response.json()["content"] == "test citation1"


def test_get_item():
    # Given
    item_id = 1

    # When
    response = client.get(f"/api/v1/pins/{item_id}/")

    # Then
    assert response.status_code == 200
    assert response.json()["id"] == item_id


def test_update_item():
    # Given
    item_id = 1
    updated_item_data = {
        "title": "Citation1 updated",
        "content": "test citation1 updated",
    }

    # When
    response = client.put(f"/api/v1/pins/{item_id}/", json=updated_item_data)

    # Then
    assert response.status_code == 200
    assert response.json()["title"] == "Citation1 updated"
    assert response.json()["content"] == "test citation1 updated"


def test_delete_item():
    # Given
    item_id = 1

    # When
    response = client.delete(f"/api/v1/pins/{item_id}/")

    # Then
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
