from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"we_are": "SlickTelemetry"}


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_get_schedule():
    response = client.get("/schedule")
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


def test_get_schedule_bad_year_no_input():
    response = client.get("/schedule/?year=")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["query", "year"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "",
                "url": "https://errors.pydantic.dev/2.5/v/int_parsing",
            }
        ]
    }


def test_get_schedule_bad_year_lower_limit():
    response = client.get("/schedule/?year=1949")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than_equal",
                "loc": ["query", "year"],
                "msg": "Input should be greater than or equal to 1950",
                "input": "1949",
                "ctx": {"ge": 1950},
                "url": "https://errors.pydantic.dev/2.5/v/greater_than_equal",
            }
        ]
    }


def test_get_schedule_bad_year_upper_limit():
    current_year = datetime.today().year
    bad_year = current_year + 1
    response = client.get(f"/schedule/?year={bad_year}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "less_than_equal",
                "loc": ["query", "year"],
                "msg": "Input should be less than or equal to 2024",
                "input": "2025",
                "ctx": {"le": 2024},
                "url": "https://errors.pydantic.dev/2.5/v/less_than_equal",
            }
        ]
    }
