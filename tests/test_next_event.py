# External
from fastapi import status

# App
from . import client_with_auth


def test_get_next_event():
    response = client_with_auth.get("/next-event")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "RoundNumber": 5,
        "Country": "China",
        "Location": "Shanghai",
        "OfficialEventName": "FORMULA 1 LENOVO CHINESE GRAND PRIX 2024",
        "EventDate": "2024-04-21 00:00:00",
        "EventName": "Chinese Grand Prix",
        "EventFormat": "sprint_shootout",
        "Session1": "Practice 1",
        "Session1Date": "2024-04-19 11:30:00+08:00",
        "Session1DateUtc": "2024-04-19 03:30:00",
        "Session2": "Sprint Shootout",
        "Session2Date": "2024-04-19 15:30:00+08:00",
        "Session2DateUtc": "2024-04-19 07:30:00",
        "Session3": "Sprint",
        "Session3Date": "2024-04-20 11:00:00+08:00",
        "Session3DateUtc": "2024-04-20 03:00:00",
        "Session4": "Qualifying",
        "Session4Date": "2024-04-20 15:00:00+08:00",
        "Session4DateUtc": "2024-04-20 07:00:00",
        "Session5": "Race",
        "Session5Date": "2024-04-21 15:00:00+08:00",
        "Session5DateUtc": "2024-04-21 07:00:00",
        "F1ApiSupport": True,
    }
