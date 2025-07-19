import os
from pathlib import Path
from fastapi.testclient import TestClient
import pytest

# Configure a temporary SQLite database for tests
os.environ["SQLALCHEMY_DATABASE_URL"] = "sqlite:///./test_api.db"

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def teardown_module(module):
    Path("test_api.db").unlink(missing_ok=True)


def test_create_and_get_horse(client):
    # Create a horse
    response = client.post("/api/v1/horses/", json={"name": "Test Horse"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Horse"

    horse_id = data["id"]

    # Retrieve the same horse
    get_resp = client.get(f"/api/v1/horses/{horse_id}")
    assert get_resp.status_code == 200
    get_data = get_resp.json()
    assert get_data["id"] == horse_id
    assert get_data["name"] == "Test Horse"


