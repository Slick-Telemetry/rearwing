from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"We Are": "SlickTelemetry"}


def test_get_schedule():
    response = client.get("/schedule/2023")
    assert response.status_code == 200
    assert response.json()[0] == {
        "RoundNumber": 0,
        "Country": "Bahrain",
        "Location": "Sakhir",
        "OfficialEventName": "FORMULA 1 ARAMCO PRE-SEASON TESTING 2023",
        "EventDate": "2023-02-25",
        "EventName": "Pre-Season Testing",
        "EventFormat": "testing",
        "Session1": "Practice 1",
        "Session1Date": "2023-02-23 10:00:00+03:00",
        "Session1DateUtc": "2023-02-23 07:00:00",
        "Session2": "Practice 2",
        "Session2Date": "2023-02-24 10:00:00+03:00",
        "Session2DateUtc": "2023-02-24 07:00:00",
        "Session3": "Practice 3",
        "Session3Date": "2023-02-25 10:00:00+03:00",
        "Session3DateUtc": "2023-02-25 07:00:00",
        "Session4": "None",
        "Session4Date": "NaT",
        "Session4DateUtc": "NaT",
        "Session5": "None",
        "Session5Date": "NaT",
        "Session5DateUtc": "NaT",
        "F1ApiSupport": True,
    }


def test_get_schedule_bad_year_lower_limit():
    response = client.get("/schedule/1949")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than",
                "loc": ["path", "year"],
                "msg": "Input should be greater than 1949",
                "input": "1949",
                "ctx": {"gt": 1949},
                "url": "https://errors.pydantic.dev/2.5/v/greater_than",
            }
        ]
    }
