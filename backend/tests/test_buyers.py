from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_buyers():
    res = client.get("/buyers")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_create_buyer():
    payload = {
        "name": "Test Buyer",
        "email": "buyer@example.com",
        "criteria": ["3 bed", "fixer"]
    }
    res = client.post("/buyers", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["name"] == payload["name"]
    assert "id" in data
