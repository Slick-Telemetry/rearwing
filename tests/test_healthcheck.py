# External
from fastapi import status
from fastapi.testclient import TestClient

# Project
from app.main import app


client = TestClient(app)


# region healthcheck


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "OK"}


# endregion healtcheck
