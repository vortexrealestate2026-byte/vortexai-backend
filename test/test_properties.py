from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_properties():
    res = client.get("/properties")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
