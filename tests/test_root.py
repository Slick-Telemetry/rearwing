# External
from fastapi.testclient import TestClient

# Project
from app.main import app


client = TestClient(app)


def test_read_root(snapshot):
    response = client.get("/")
    snapshot.assert_match(response.json())
