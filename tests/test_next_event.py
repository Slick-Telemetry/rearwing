# External
from fastapi import status

# App
from . import client_with_auth


def test_get_next_event():
    response = client_with_auth.get("/next-event")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "RoundNumber": 4,
        "Country": "Japan",
        "Location": "Suzuka",
        "OfficialEventName": "FORMULA 1 MSC CRUISES JAPANESE GRAND PRIX 2024",
        "EventDate": "2024-04-07 00:00:00",
        "EventName": "Japanese Grand Prix",
        "EventFormat": "conventional",
        "Session1": "Practice 1",
        "Session1Date": "2024-04-05 11:30:00+09:00",
        "Session1DateUtc": "2024-04-05 02:30:00",
        "Session2": "Practice 2",
        "Session2Date": "2024-04-05 15:00:00+09:00",
        "Session2DateUtc": "2024-04-05 06:00:00",
        "Session3": "Practice 3",
        "Session3Date": "2024-04-06 11:30:00+09:00",
        "Session3DateUtc": "2024-04-06 02:30:00",
        "Session4": "Qualifying",
        "Session4Date": "2024-04-06 15:00:00+09:00",
        "Session4DateUtc": "2024-04-06 06:00:00",
        "Session5": "Race",
        "Session5Date": "2024-04-07 14:00:00+09:00",
        "Session5DateUtc": "2024-04-07 05:00:00",
        "F1ApiSupport": True,
    }
