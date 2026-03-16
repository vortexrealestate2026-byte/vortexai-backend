from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_deals():
    res = client.get("/deals")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_filter_deals():
    res = client.get("/deals?min_score=70")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
