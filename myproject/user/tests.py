from django.test import TestCase

# Create your tests here.
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


def test_user_list_get(api_client):
    response = api_client.get("/api/users/")

    assert response.status_code == 200
    assert response.data == {"message": "Hello World"}


def test_user_list_post(api_client):
    response = api_client.post(
        "/api/users/",
        {"name": "Alice", "email": "alice@example.com", "password": "secret"},
        format="json",
    )

    assert response.status_code == 200
    assert response.data == {"message": "Hello World POST"}
