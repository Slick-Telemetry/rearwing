# External
from fastapi import status
from fastapi.testclient import TestClient

# App
from . import client


def test_get_schedule():
    response = client.get("/schedule")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["year"] == 2024
    assert response.json()["EventSchedule"][0] == {
        "RoundNumber": 1,
        "Country": "Bahrain",
        "Location": "Sakhir",
        "OfficialEventName": "FORMULA 1 GULF AIR BAHRAIN GRAND PRIX 2024",
        "EventDate": "2024-03-02",
        "EventName": "Bahrain Grand Prix",
        "EventFormat": "conventional",
        "Session1": "Practice 1",
        "Session1Date": "2024-02-29 14:30:00+03:00",
        "Session1DateUtc": "2024-02-29 11:30:00",
        "Session2": "Practice 2",
        "Session2Date": "2024-02-29 18:00:00+03:00",
        "Session2DateUtc": "2024-02-29 15:00:00",
        "Session3": "Practice 3",
        "Session3Date": "2024-03-01 15:30:00+03:00",
        "Session3DateUtc": "2024-03-01 12:30:00",
        "Session4": "Qualifying",
        "Session4Date": "2024-03-01 19:00:00+03:00",
        "Session4DateUtc": "2024-03-01 16:00:00",
        "Session5": "Race",
        "Session5Date": "2024-03-02 18:00:00+03:00",
        "Session5DateUtc": "2024-03-02 15:00:00",
        "F1ApiSupport": True,
    }


def test_get_schedule_good_year():
    response = client.get("/schedule?year=2023")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["year"] == 2023
    assert response.json()["EventSchedule"][0] == {
        "RoundNumber": 1,
        "Country": "Bahrain",
        "Location": "Sakhir",
        "OfficialEventName": "FORMULA 1 GULF AIR BAHRAIN GRAND PRIX 2023",
        "EventDate": "2023-03-05",
        "EventName": "Bahrain Grand Prix",
        "EventFormat": "conventional",
        "Session1": "Practice 1",
        "Session1Date": "2023-03-03 14:30:00+03:00",
        "Session1DateUtc": "2023-03-03 11:30:00",
        "Session2": "Practice 2",
        "Session2Date": "2023-03-03 18:00:00+03:00",
        "Session2DateUtc": "2023-03-03 15:00:00",
        "Session3": "Practice 3",
        "Session3Date": "2023-03-04 14:30:00+03:00",
        "Session3DateUtc": "2023-03-04 11:30:00",
        "Session4": "Qualifying",
        "Session4Date": "2023-03-04 18:00:00+03:00",
        "Session4DateUtc": "2023-03-04 15:00:00",
        "Session5": "Race",
        "Session5Date": "2023-03-05 18:00:00+03:00",
        "Session5DateUtc": "2023-03-05 15:00:00",
        "F1ApiSupport": True,
    }
