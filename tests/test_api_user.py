# test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    # Given
    item_data = {"username": "Hydra", "email": "hydra@gmail.com", "password": "hydrahydra"}

    # When
    response = client.post("/api/v1/users", json=item_data)

    # Then
    assert response.status_code == 200
    assert response.json()["username"] == "Hydra"
    assert response.json()["email"] == "hydra@gmail.com"


def test_login():
    item_data = {"user": {"email": "hydra@gmail.com", "password": "hydrahydra"}}

    # When
    response = client.post(f"/api/v1/users/login", json=item_data)

    # Then
    assert response.status_code == 200
    assert response.json()["user"]["username"] == "Hydra"


def test_get_user():
    id_user = 1

    # When
    response = client.get(f"/api/v1/user/{id_user}")

    # Then
    assert response.status_code == 200
    assert response.json()["id"] == id_user


def test_update_user():
    # Given
    updated_item_data = {"user": {"email": "hydra56@gmail.com"}}

    # When
    response = client.put(f"/api/v1/user", json=updated_item_data)

    # Then
    assert response.status_code == 200
    assert response.json()["user"]["email"] == "hydra56@gmail.com"
