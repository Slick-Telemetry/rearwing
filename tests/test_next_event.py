# External
from fastapi import status
from fastapi.testclient import TestClient

# App
from . import client


def test_get_next_event():
    response = client.get("/next-event")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "RoundNumber": 3,
        "Country": "Australia",
        "Location": "Melbourne",
        "OfficialEventName": "FORMULA 1 ROLEX AUSTRALIAN GRAND PRIX 2024",
        "EventDate": "2024-03-24 00:00:00",
        "EventName": "Australian Grand Prix",
        "EventFormat": "conventional",
        "Session1": "Practice 1",
        "Session1Date": "2024-03-22 12:30:00+11:00",
        "Session1DateUtc": "2024-03-22 01:30:00",
        "Session2": "Practice 2",
        "Session2Date": "2024-03-22 16:00:00+11:00",
        "Session2DateUtc": "2024-03-22 05:00:00",
        "Session3": "Practice 3",
        "Session3Date": "2024-03-23 12:30:00+11:00",
        "Session3DateUtc": "2024-03-23 01:30:00",
        "Session4": "Qualifying",
        "Session4Date": "2024-03-23 16:00:00+11:00",
        "Session4DateUtc": "2024-03-23 05:00:00",
        "Session5": "Race",
        "Session5Date": "2024-03-24 15:00:00+11:00",
        "Session5DateUtc": "2024-03-24 04:00:00",
        "F1ApiSupport": True,
    }
