# External
from fastapi import status
from fastapi.testclient import TestClient

# Project
from app.main import app


client = TestClient(app)


# region good inputs


def test_get_telemetry():
    response = client.get("/telemetry/2023/4/1/1?session=5&weather=false")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["Telemetry"][0] == {
        "Time": 0,
        "RPM": 10115,
        "Speed": 0.0,
        "nGear": 1,
        "Throttle": 16.0,
        "Brake": False,
        "DRS": 1,
        "Distance": 0.0019578773,
        "X": 1811.0527567522,
        "Y": -279.9800289003,
    }
    assert response.json()["Weather"] == None


def test_get_telemetry_with_weather():
    response = client.get("/telemetry/2023/4/1/1?session=5&weather=true")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["Telemetry"][0] == {
        "Time": 0,
        "RPM": 10115,
        "Speed": 0.0,
        "nGear": 1,
        "Throttle": 16.0,
        "Brake": False,
        "DRS": 1,
        "Distance": 0.0019578773,
        "X": 1811.0527567522,
        "Y": -279.9800289003,
    }
    assert response.json()["Weather"] == {
        "Time": 3790336,
        "AirTemp": 24.9,
        "Humidity": 49.0,
        "Pressure": 1008.7,
        "Rainfall": False,
        "TrackTemp": 43.4,
        "WindDirection": 50,
        "WindSpeed": 0.8,
    }


# endregion good inputs

# region bad inputs


def test_get_telemetry_bad_round():
    response = client.get("/telemetry/2023/25/1/1?session=5&weather=false")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Bad Request. Invalid round: 25"}


def test_get_telemetry_bad_driver_number():
    response = client.get("/telemetry/2023/4/3/1?session=5&weather=false")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Laps for driver 3 not found."}


def test_get_telemetry_bad_lap():
    response = client.get("/telemetry/2023/4/1/80?session=5&weather=false")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Requested lap for driver 1 not found."}


# endregion bad inputs
