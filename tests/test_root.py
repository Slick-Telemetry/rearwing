# External
from fastapi import status
from fastapi.testclient import TestClient

# Project
from app.main import app


client = TestClient(app)


# region root


def test_read_root():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"we_are": "SlickTelemetry"}


# endregion root
