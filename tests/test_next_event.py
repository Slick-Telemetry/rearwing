# External
from fastapi import status
from fastapi.testclient import TestClient

# Project
from app.main import app


client = TestClient(app)


def test_get_next_event():
    response = client.get("/next-event")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "RoundNumber": 2,
        "Country": "Saudi Arabia",
        "Location": "Jeddah",
        "OfficialEventName": "FORMULA 1 STC SAUDI ARABIAN GRAND PRIX 2024",
        "EventDate": "2024-03-09 00:00:00",
        "EventName": "Saudi Arabian Grand Prix",
        "EventFormat": "conventional",
        "Session1": "Practice 1",
        "Session1Date": "2024-03-07 16:30:00+03:00",
        "Session1DateUtc": "2024-03-07 13:30:00",
        "Session2": "Practice 2",
        "Session2Date": "2024-03-07 20:00:00+03:00",
        "Session2DateUtc": "2024-03-07 17:00:00",
        "Session3": "Practice 3",
        "Session3Date": "2024-03-08 16:30:00+03:00",
        "Session3DateUtc": "2024-03-08 13:30:00",
        "Session4": "Qualifying",
        "Session4Date": "2024-03-08 20:00:00+03:00",
        "Session4DateUtc": "2024-03-08 17:00:00",
        "Session5": "Race",
        "Session5Date": "2024-03-09 20:00:00+03:00",
        "Session5DateUtc": "2024-03-09 17:00:00",
        "F1ApiSupport": True,
    }
