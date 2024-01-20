from datetime import datetime

from fastapi.testclient import TestClient

from app.constants import (
    MAX_SUPPORTED_ROUND,
    MAX_SUPPORTED_YEAR,
    MIN_SUPPORTED_ROUND,
    MIN_SUPPORTED_YEAR,
)
from app.main import app

client = TestClient(app)


# region root


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"we_are": "SlickTelemetry"}


# endregion root


# region healtcheck


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


# endregion healtcheck


# region schedule

# region schedule - good inputs


def test_get_schedule():
    response = client.get("/schedule")
    assert response.status_code == 200
    assert response.json() == [
        {
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
        },
        {
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
        },
        {
            "RoundNumber": 2,
            "Country": "Saudi Arabia",
            "Location": "Jeddah",
            "OfficialEventName": "FORMULA 1 STC SAUDI ARABIAN GRAND PRIX 2023",
            "EventDate": "2023-03-19",
            "EventName": "Saudi Arabian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-03-17 16:30:00+03:00",
            "Session1DateUtc": "2023-03-17 13:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-03-17 20:00:00+03:00",
            "Session2DateUtc": "2023-03-17 17:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-03-18 16:30:00+03:00",
            "Session3DateUtc": "2023-03-18 13:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-03-18 20:00:00+03:00",
            "Session4DateUtc": "2023-03-18 17:00:00",
            "Session5": "Race",
            "Session5Date": "2023-03-19 20:00:00+03:00",
            "Session5DateUtc": "2023-03-19 17:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 3,
            "Country": "Australia",
            "Location": "Melbourne",
            "OfficialEventName": "FORMULA 1 ROLEX AUSTRALIAN GRAND PRIX 2023",
            "EventDate": "2023-04-02",
            "EventName": "Australian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-03-31 12:30:00+10:00",
            "Session1DateUtc": "2023-03-31 02:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-03-31 16:00:00+10:00",
            "Session2DateUtc": "2023-03-31 06:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-04-01 12:30:00+10:00",
            "Session3DateUtc": "2023-04-01 02:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-04-01 16:00:00+10:00",
            "Session4DateUtc": "2023-04-01 06:00:00",
            "Session5": "Race",
            "Session5Date": "2023-04-02 15:00:00+10:00",
            "Session5DateUtc": "2023-04-02 05:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 4,
            "Country": "Azerbaijan",
            "Location": "Baku",
            "OfficialEventName": "FORMULA 1 AZERBAIJAN GRAND PRIX 2023",
            "EventDate": "2023-04-30",
            "EventName": "Azerbaijan Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-04-28 13:30:00+04:00",
            "Session1DateUtc": "2023-04-28 09:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-04-28 17:00:00+04:00",
            "Session2DateUtc": "2023-04-28 13:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-04-29 12:30:00+04:00",
            "Session3DateUtc": "2023-04-29 08:30:00",
            "Session4": "Sprint",
            "Session4Date": "2023-04-29 17:30:00+04:00",
            "Session4DateUtc": "2023-04-29 13:30:00",
            "Session5": "Race",
            "Session5Date": "2023-04-30 15:00:00+04:00",
            "Session5DateUtc": "2023-04-30 11:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 5,
            "Country": "United States",
            "Location": "Miami",
            "OfficialEventName": "FORMULA 1 CRYPTO.COM MIAMI GRAND PRIX 2023",
            "EventDate": "2023-05-07",
            "EventName": "Miami Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-05-05 14:00:00-04:00",
            "Session1DateUtc": "2023-05-05 18:00:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-05-05 17:30:00-04:00",
            "Session2DateUtc": "2023-05-05 21:30:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-05-06 12:30:00-04:00",
            "Session3DateUtc": "2023-05-06 16:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-05-06 16:00:00-04:00",
            "Session4DateUtc": "2023-05-06 20:00:00",
            "Session5": "Race",
            "Session5Date": "2023-05-07 15:30:00-04:00",
            "Session5DateUtc": "2023-05-07 19:30:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 6,
            "Country": "Monaco",
            "Location": "Monaco",
            "OfficialEventName": "FORMULA 1 GRAND PRIX DE MONACO 2023",
            "EventDate": "2023-05-28",
            "EventName": "Monaco Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-05-26 13:30:00+02:00",
            "Session1DateUtc": "2023-05-26 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-05-26 17:00:00+02:00",
            "Session2DateUtc": "2023-05-26 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-05-27 12:30:00+02:00",
            "Session3DateUtc": "2023-05-27 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-05-27 16:00:00+02:00",
            "Session4DateUtc": "2023-05-27 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-05-28 15:00:00+02:00",
            "Session5DateUtc": "2023-05-28 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 7,
            "Country": "Spain",
            "Location": "Barcelona",
            "OfficialEventName": "FORMULA 1 AWS GRAN PREMIO DE ESPAÑA 2023",
            "EventDate": "2023-06-04",
            "EventName": "Spanish Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-06-02 13:30:00+02:00",
            "Session1DateUtc": "2023-06-02 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-06-02 17:00:00+02:00",
            "Session2DateUtc": "2023-06-02 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-06-03 12:30:00+02:00",
            "Session3DateUtc": "2023-06-03 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-06-03 16:00:00+02:00",
            "Session4DateUtc": "2023-06-03 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-06-04 15:00:00+02:00",
            "Session5DateUtc": "2023-06-04 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 8,
            "Country": "Canada",
            "Location": "Montréal",
            "OfficialEventName": "FORMULA 1 PIRELLI GRAND PRIX DU CANADA 2023",
            "EventDate": "2023-06-18",
            "EventName": "Canadian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-06-16 13:30:00-04:00",
            "Session1DateUtc": "2023-06-16 17:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-06-16 16:30:00-04:00",
            "Session2DateUtc": "2023-06-16 20:30:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-06-17 12:30:00-04:00",
            "Session3DateUtc": "2023-06-17 16:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-06-17 16:00:00-04:00",
            "Session4DateUtc": "2023-06-17 20:00:00",
            "Session5": "Race",
            "Session5Date": "2023-06-18 14:00:00-04:00",
            "Session5DateUtc": "2023-06-18 18:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 9,
            "Country": "Austria",
            "Location": "Spielberg",
            "OfficialEventName": "FORMULA 1 ROLEX GROSSER PREIS VON ÖSTERREICH 2023",
            "EventDate": "2023-07-02",
            "EventName": "Austrian Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-06-30 13:30:00+02:00",
            "Session1DateUtc": "2023-06-30 11:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-06-30 17:00:00+02:00",
            "Session2DateUtc": "2023-06-30 15:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-07-01 12:00:00+02:00",
            "Session3DateUtc": "2023-07-01 10:00:00",
            "Session4": "Sprint",
            "Session4Date": "2023-07-01 16:30:00+02:00",
            "Session4DateUtc": "2023-07-01 14:30:00",
            "Session5": "Race",
            "Session5Date": "2023-07-02 15:00:00+02:00",
            "Session5DateUtc": "2023-07-02 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 10,
            "Country": "Great Britain",
            "Location": "Silverstone",
            "OfficialEventName": "FORMULA 1 ARAMCO BRITISH GRAND PRIX 2023",
            "EventDate": "2023-07-09",
            "EventName": "British Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-07-07 12:30:00+01:00",
            "Session1DateUtc": "2023-07-07 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-07-07 16:00:00+01:00",
            "Session2DateUtc": "2023-07-07 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-07-08 11:30:00+01:00",
            "Session3DateUtc": "2023-07-08 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-07-08 15:00:00+01:00",
            "Session4DateUtc": "2023-07-08 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-07-09 15:00:00+01:00",
            "Session5DateUtc": "2023-07-09 14:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 11,
            "Country": "Hungary",
            "Location": "Budapest",
            "OfficialEventName": "FORMULA 1 QATAR AIRWAYS HUNGARIAN GRAND PRIX 2023",
            "EventDate": "2023-07-23",
            "EventName": "Hungarian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-07-21 13:30:00+02:00",
            "Session1DateUtc": "2023-07-21 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-07-21 17:00:00+02:00",
            "Session2DateUtc": "2023-07-21 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-07-22 12:30:00+02:00",
            "Session3DateUtc": "2023-07-22 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-07-22 16:00:00+02:00",
            "Session4DateUtc": "2023-07-22 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-07-23 15:00:00+02:00",
            "Session5DateUtc": "2023-07-23 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 12,
            "Country": "Belgium",
            "Location": "Spa-Francorchamps",
            "OfficialEventName": "FORMULA 1 MSC CRUISES BELGIAN GRAND PRIX 2023",
            "EventDate": "2023-07-30",
            "EventName": "Belgian Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-07-28 13:30:00+02:00",
            "Session1DateUtc": "2023-07-28 11:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-07-28 17:00:00+02:00",
            "Session2DateUtc": "2023-07-28 15:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-07-29 12:00:00+02:00",
            "Session3DateUtc": "2023-07-29 10:00:00",
            "Session4": "Sprint",
            "Session4Date": "2023-07-29 17:05:00+02:00",
            "Session4DateUtc": "2023-07-29 15:05:00",
            "Session5": "Race",
            "Session5Date": "2023-07-30 15:00:00+02:00",
            "Session5DateUtc": "2023-07-30 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 13,
            "Country": "Netherlands",
            "Location": "Zandvoort",
            "OfficialEventName": "FORMULA 1 HEINEKEN DUTCH GRAND PRIX 2023",
            "EventDate": "2023-08-27",
            "EventName": "Dutch Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-08-25 12:30:00+02:00",
            "Session1DateUtc": "2023-08-25 10:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-08-25 16:00:00+02:00",
            "Session2DateUtc": "2023-08-25 14:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-08-26 11:30:00+02:00",
            "Session3DateUtc": "2023-08-26 09:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-08-26 15:00:00+02:00",
            "Session4DateUtc": "2023-08-26 13:00:00",
            "Session5": "Race",
            "Session5Date": "2023-08-27 15:00:00+02:00",
            "Session5DateUtc": "2023-08-27 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 14,
            "Country": "Italy",
            "Location": "Monza",
            "OfficialEventName": "FORMULA 1 PIRELLI GRAN PREMIO D’ITALIA 2023 ",
            "EventDate": "2023-09-03",
            "EventName": "Italian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-09-01 13:30:00+02:00",
            "Session1DateUtc": "2023-09-01 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-09-01 17:00:00+02:00",
            "Session2DateUtc": "2023-09-01 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-09-02 12:30:00+02:00",
            "Session3DateUtc": "2023-09-02 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-09-02 16:00:00+02:00",
            "Session4DateUtc": "2023-09-02 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-09-03 15:00:00+02:00",
            "Session5DateUtc": "2023-09-03 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 15,
            "Country": "Singapore",
            "Location": "Marina Bay",
            "OfficialEventName": "FORMULA 1 SINGAPORE AIRLINES SINGAPORE GRAND PRIX 2023 ",
            "EventDate": "2023-09-17",
            "EventName": "Singapore Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-09-15 17:30:00+08:00",
            "Session1DateUtc": "2023-09-15 09:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-09-15 21:00:00+08:00",
            "Session2DateUtc": "2023-09-15 13:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-09-16 17:30:00+08:00",
            "Session3DateUtc": "2023-09-16 09:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-09-16 21:00:00+08:00",
            "Session4DateUtc": "2023-09-16 13:00:00",
            "Session5": "Race",
            "Session5Date": "2023-09-17 20:00:00+08:00",
            "Session5DateUtc": "2023-09-17 12:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 16,
            "Country": "Japan",
            "Location": "Suzuka",
            "OfficialEventName": "FORMULA 1 LENOVO JAPANESE GRAND PRIX 2023 ",
            "EventDate": "2023-09-24",
            "EventName": "Japanese Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-09-22 11:30:00+09:00",
            "Session1DateUtc": "2023-09-22 02:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-09-22 15:00:00+09:00",
            "Session2DateUtc": "2023-09-22 06:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-09-23 11:30:00+09:00",
            "Session3DateUtc": "2023-09-23 02:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-09-23 15:00:00+09:00",
            "Session4DateUtc": "2023-09-23 06:00:00",
            "Session5": "Race",
            "Session5Date": "2023-09-24 14:00:00+09:00",
            "Session5DateUtc": "2023-09-24 05:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 17,
            "Country": "Qatar",
            "Location": "Lusail",
            "OfficialEventName": "FORMULA 1 QATAR AIRWAYS QATAR GRAND PRIX 2023",
            "EventDate": "2023-10-08",
            "EventName": "Qatar Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-10-06 16:30:00+03:00",
            "Session1DateUtc": "2023-10-06 13:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-10-06 20:00:00+03:00",
            "Session2DateUtc": "2023-10-06 17:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-10-07 16:20:00+03:00",
            "Session3DateUtc": "2023-10-07 13:20:00",
            "Session4": "Sprint",
            "Session4Date": "2023-10-07 20:30:00+03:00",
            "Session4DateUtc": "2023-10-07 17:30:00",
            "Session5": "Race",
            "Session5Date": "2023-10-08 20:00:00+03:00",
            "Session5DateUtc": "2023-10-08 17:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 18,
            "Country": "United States",
            "Location": "Austin",
            "OfficialEventName": "FORMULA 1 LENOVO UNITED STATES GRAND PRIX 2023",
            "EventDate": "2023-10-22",
            "EventName": "United States Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-10-20 12:30:00-05:00",
            "Session1DateUtc": "2023-10-20 17:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-10-20 16:00:00-05:00",
            "Session2DateUtc": "2023-10-20 21:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-10-21 12:30:00-05:00",
            "Session3DateUtc": "2023-10-21 17:30:00",
            "Session4": "Sprint",
            "Session4Date": "2023-10-21 17:00:00-05:00",
            "Session4DateUtc": "2023-10-21 22:00:00",
            "Session5": "Race",
            "Session5Date": "2023-10-22 14:00:00-05:00",
            "Session5DateUtc": "2023-10-22 19:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 19,
            "Country": "Mexico",
            "Location": "Mexico City",
            "OfficialEventName": "FORMULA 1 GRAN PREMIO DE LA CIUDAD DE MÉXICO 2023",
            "EventDate": "2023-10-29",
            "EventName": "Mexico City Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-10-27 12:30:00-06:00",
            "Session1DateUtc": "2023-10-27 18:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-10-27 16:00:00-06:00",
            "Session2DateUtc": "2023-10-27 22:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-10-28 11:30:00-06:00",
            "Session3DateUtc": "2023-10-28 17:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-10-28 15:00:00-06:00",
            "Session4DateUtc": "2023-10-28 21:00:00",
            "Session5": "Race",
            "Session5Date": "2023-10-29 14:00:00-06:00",
            "Session5DateUtc": "2023-10-29 20:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 20,
            "Country": "Brazil",
            "Location": "São Paulo",
            "OfficialEventName": "FORMULA 1 ROLEX GRANDE PRÊMIO DE SÃO PAULO 2023",
            "EventDate": "2023-11-05",
            "EventName": "São Paulo Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-11-03 11:30:00-03:00",
            "Session1DateUtc": "2023-11-03 14:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-11-03 15:00:00-03:00",
            "Session2DateUtc": "2023-11-03 18:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-11-04 11:00:00-03:00",
            "Session3DateUtc": "2023-11-04 14:00:00",
            "Session4": "Sprint",
            "Session4Date": "2023-11-04 15:30:00-03:00",
            "Session4DateUtc": "2023-11-04 18:30:00",
            "Session5": "Race",
            "Session5Date": "2023-11-05 14:00:00-03:00",
            "Session5DateUtc": "2023-11-05 17:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 21,
            "Country": "United States",
            "Location": "Las Vegas",
            "OfficialEventName": "FORMULA 1 HEINEKEN SILVER LAS VEGAS GRAND PRIX 2023",
            "EventDate": "2023-11-18",
            "EventName": "Las Vegas Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-11-16 20:30:00-08:00",
            "Session1DateUtc": "2023-11-17 04:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-11-17 02:30:00-08:00",
            "Session2DateUtc": "2023-11-17 10:30:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-11-17 20:30:00-08:00",
            "Session3DateUtc": "2023-11-18 04:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-11-18 00:00:00-08:00",
            "Session4DateUtc": "2023-11-18 08:00:00",
            "Session5": "Race",
            "Session5Date": "2023-11-18 22:00:00-08:00",
            "Session5DateUtc": "2023-11-19 06:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 22,
            "Country": "Abu Dhabi",
            "Location": "Yas Island",
            "OfficialEventName": "FORMULA 1 ETIHAD AIRWAYS ABU DHABI GRAND PRIX 2023 ",
            "EventDate": "2023-11-26",
            "EventName": "Abu Dhabi Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-11-24 13:30:00+04:00",
            "Session1DateUtc": "2023-11-24 09:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-11-24 17:00:00+04:00",
            "Session2DateUtc": "2023-11-24 13:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-11-25 14:30:00+04:00",
            "Session3DateUtc": "2023-11-25 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-11-25 18:00:00+04:00",
            "Session4DateUtc": "2023-11-25 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-11-26 17:00:00+04:00",
            "Session5DateUtc": "2023-11-26 13:00:00",
            "F1ApiSupport": True,
        },
    ]


def test_get_schedule_good_year():
    response = client.get("/schedule?year=2023")
    assert response.status_code == 200
    assert response.json() == [
        {
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
        },
        {
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
        },
        {
            "RoundNumber": 2,
            "Country": "Saudi Arabia",
            "Location": "Jeddah",
            "OfficialEventName": "FORMULA 1 STC SAUDI ARABIAN GRAND PRIX 2023",
            "EventDate": "2023-03-19",
            "EventName": "Saudi Arabian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-03-17 16:30:00+03:00",
            "Session1DateUtc": "2023-03-17 13:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-03-17 20:00:00+03:00",
            "Session2DateUtc": "2023-03-17 17:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-03-18 16:30:00+03:00",
            "Session3DateUtc": "2023-03-18 13:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-03-18 20:00:00+03:00",
            "Session4DateUtc": "2023-03-18 17:00:00",
            "Session5": "Race",
            "Session5Date": "2023-03-19 20:00:00+03:00",
            "Session5DateUtc": "2023-03-19 17:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 3,
            "Country": "Australia",
            "Location": "Melbourne",
            "OfficialEventName": "FORMULA 1 ROLEX AUSTRALIAN GRAND PRIX 2023",
            "EventDate": "2023-04-02",
            "EventName": "Australian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-03-31 12:30:00+10:00",
            "Session1DateUtc": "2023-03-31 02:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-03-31 16:00:00+10:00",
            "Session2DateUtc": "2023-03-31 06:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-04-01 12:30:00+10:00",
            "Session3DateUtc": "2023-04-01 02:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-04-01 16:00:00+10:00",
            "Session4DateUtc": "2023-04-01 06:00:00",
            "Session5": "Race",
            "Session5Date": "2023-04-02 15:00:00+10:00",
            "Session5DateUtc": "2023-04-02 05:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 4,
            "Country": "Azerbaijan",
            "Location": "Baku",
            "OfficialEventName": "FORMULA 1 AZERBAIJAN GRAND PRIX 2023",
            "EventDate": "2023-04-30",
            "EventName": "Azerbaijan Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-04-28 13:30:00+04:00",
            "Session1DateUtc": "2023-04-28 09:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-04-28 17:00:00+04:00",
            "Session2DateUtc": "2023-04-28 13:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-04-29 12:30:00+04:00",
            "Session3DateUtc": "2023-04-29 08:30:00",
            "Session4": "Sprint",
            "Session4Date": "2023-04-29 17:30:00+04:00",
            "Session4DateUtc": "2023-04-29 13:30:00",
            "Session5": "Race",
            "Session5Date": "2023-04-30 15:00:00+04:00",
            "Session5DateUtc": "2023-04-30 11:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 5,
            "Country": "United States",
            "Location": "Miami",
            "OfficialEventName": "FORMULA 1 CRYPTO.COM MIAMI GRAND PRIX 2023",
            "EventDate": "2023-05-07",
            "EventName": "Miami Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-05-05 14:00:00-04:00",
            "Session1DateUtc": "2023-05-05 18:00:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-05-05 17:30:00-04:00",
            "Session2DateUtc": "2023-05-05 21:30:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-05-06 12:30:00-04:00",
            "Session3DateUtc": "2023-05-06 16:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-05-06 16:00:00-04:00",
            "Session4DateUtc": "2023-05-06 20:00:00",
            "Session5": "Race",
            "Session5Date": "2023-05-07 15:30:00-04:00",
            "Session5DateUtc": "2023-05-07 19:30:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 6,
            "Country": "Monaco",
            "Location": "Monaco",
            "OfficialEventName": "FORMULA 1 GRAND PRIX DE MONACO 2023",
            "EventDate": "2023-05-28",
            "EventName": "Monaco Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-05-26 13:30:00+02:00",
            "Session1DateUtc": "2023-05-26 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-05-26 17:00:00+02:00",
            "Session2DateUtc": "2023-05-26 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-05-27 12:30:00+02:00",
            "Session3DateUtc": "2023-05-27 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-05-27 16:00:00+02:00",
            "Session4DateUtc": "2023-05-27 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-05-28 15:00:00+02:00",
            "Session5DateUtc": "2023-05-28 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 7,
            "Country": "Spain",
            "Location": "Barcelona",
            "OfficialEventName": "FORMULA 1 AWS GRAN PREMIO DE ESPAÑA 2023",
            "EventDate": "2023-06-04",
            "EventName": "Spanish Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-06-02 13:30:00+02:00",
            "Session1DateUtc": "2023-06-02 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-06-02 17:00:00+02:00",
            "Session2DateUtc": "2023-06-02 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-06-03 12:30:00+02:00",
            "Session3DateUtc": "2023-06-03 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-06-03 16:00:00+02:00",
            "Session4DateUtc": "2023-06-03 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-06-04 15:00:00+02:00",
            "Session5DateUtc": "2023-06-04 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 8,
            "Country": "Canada",
            "Location": "Montréal",
            "OfficialEventName": "FORMULA 1 PIRELLI GRAND PRIX DU CANADA 2023",
            "EventDate": "2023-06-18",
            "EventName": "Canadian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-06-16 13:30:00-04:00",
            "Session1DateUtc": "2023-06-16 17:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-06-16 16:30:00-04:00",
            "Session2DateUtc": "2023-06-16 20:30:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-06-17 12:30:00-04:00",
            "Session3DateUtc": "2023-06-17 16:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-06-17 16:00:00-04:00",
            "Session4DateUtc": "2023-06-17 20:00:00",
            "Session5": "Race",
            "Session5Date": "2023-06-18 14:00:00-04:00",
            "Session5DateUtc": "2023-06-18 18:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 9,
            "Country": "Austria",
            "Location": "Spielberg",
            "OfficialEventName": "FORMULA 1 ROLEX GROSSER PREIS VON ÖSTERREICH 2023",
            "EventDate": "2023-07-02",
            "EventName": "Austrian Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-06-30 13:30:00+02:00",
            "Session1DateUtc": "2023-06-30 11:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-06-30 17:00:00+02:00",
            "Session2DateUtc": "2023-06-30 15:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-07-01 12:00:00+02:00",
            "Session3DateUtc": "2023-07-01 10:00:00",
            "Session4": "Sprint",
            "Session4Date": "2023-07-01 16:30:00+02:00",
            "Session4DateUtc": "2023-07-01 14:30:00",
            "Session5": "Race",
            "Session5Date": "2023-07-02 15:00:00+02:00",
            "Session5DateUtc": "2023-07-02 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 10,
            "Country": "Great Britain",
            "Location": "Silverstone",
            "OfficialEventName": "FORMULA 1 ARAMCO BRITISH GRAND PRIX 2023",
            "EventDate": "2023-07-09",
            "EventName": "British Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-07-07 12:30:00+01:00",
            "Session1DateUtc": "2023-07-07 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-07-07 16:00:00+01:00",
            "Session2DateUtc": "2023-07-07 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-07-08 11:30:00+01:00",
            "Session3DateUtc": "2023-07-08 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-07-08 15:00:00+01:00",
            "Session4DateUtc": "2023-07-08 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-07-09 15:00:00+01:00",
            "Session5DateUtc": "2023-07-09 14:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 11,
            "Country": "Hungary",
            "Location": "Budapest",
            "OfficialEventName": "FORMULA 1 QATAR AIRWAYS HUNGARIAN GRAND PRIX 2023",
            "EventDate": "2023-07-23",
            "EventName": "Hungarian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-07-21 13:30:00+02:00",
            "Session1DateUtc": "2023-07-21 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-07-21 17:00:00+02:00",
            "Session2DateUtc": "2023-07-21 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-07-22 12:30:00+02:00",
            "Session3DateUtc": "2023-07-22 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-07-22 16:00:00+02:00",
            "Session4DateUtc": "2023-07-22 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-07-23 15:00:00+02:00",
            "Session5DateUtc": "2023-07-23 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 12,
            "Country": "Belgium",
            "Location": "Spa-Francorchamps",
            "OfficialEventName": "FORMULA 1 MSC CRUISES BELGIAN GRAND PRIX 2023",
            "EventDate": "2023-07-30",
            "EventName": "Belgian Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-07-28 13:30:00+02:00",
            "Session1DateUtc": "2023-07-28 11:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-07-28 17:00:00+02:00",
            "Session2DateUtc": "2023-07-28 15:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-07-29 12:00:00+02:00",
            "Session3DateUtc": "2023-07-29 10:00:00",
            "Session4": "Sprint",
            "Session4Date": "2023-07-29 17:05:00+02:00",
            "Session4DateUtc": "2023-07-29 15:05:00",
            "Session5": "Race",
            "Session5Date": "2023-07-30 15:00:00+02:00",
            "Session5DateUtc": "2023-07-30 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 13,
            "Country": "Netherlands",
            "Location": "Zandvoort",
            "OfficialEventName": "FORMULA 1 HEINEKEN DUTCH GRAND PRIX 2023",
            "EventDate": "2023-08-27",
            "EventName": "Dutch Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-08-25 12:30:00+02:00",
            "Session1DateUtc": "2023-08-25 10:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-08-25 16:00:00+02:00",
            "Session2DateUtc": "2023-08-25 14:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-08-26 11:30:00+02:00",
            "Session3DateUtc": "2023-08-26 09:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-08-26 15:00:00+02:00",
            "Session4DateUtc": "2023-08-26 13:00:00",
            "Session5": "Race",
            "Session5Date": "2023-08-27 15:00:00+02:00",
            "Session5DateUtc": "2023-08-27 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 14,
            "Country": "Italy",
            "Location": "Monza",
            "OfficialEventName": "FORMULA 1 PIRELLI GRAN PREMIO D’ITALIA 2023 ",
            "EventDate": "2023-09-03",
            "EventName": "Italian Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-09-01 13:30:00+02:00",
            "Session1DateUtc": "2023-09-01 11:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-09-01 17:00:00+02:00",
            "Session2DateUtc": "2023-09-01 15:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-09-02 12:30:00+02:00",
            "Session3DateUtc": "2023-09-02 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-09-02 16:00:00+02:00",
            "Session4DateUtc": "2023-09-02 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-09-03 15:00:00+02:00",
            "Session5DateUtc": "2023-09-03 13:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 15,
            "Country": "Singapore",
            "Location": "Marina Bay",
            "OfficialEventName": "FORMULA 1 SINGAPORE AIRLINES SINGAPORE GRAND PRIX 2023 ",
            "EventDate": "2023-09-17",
            "EventName": "Singapore Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-09-15 17:30:00+08:00",
            "Session1DateUtc": "2023-09-15 09:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-09-15 21:00:00+08:00",
            "Session2DateUtc": "2023-09-15 13:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-09-16 17:30:00+08:00",
            "Session3DateUtc": "2023-09-16 09:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-09-16 21:00:00+08:00",
            "Session4DateUtc": "2023-09-16 13:00:00",
            "Session5": "Race",
            "Session5Date": "2023-09-17 20:00:00+08:00",
            "Session5DateUtc": "2023-09-17 12:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 16,
            "Country": "Japan",
            "Location": "Suzuka",
            "OfficialEventName": "FORMULA 1 LENOVO JAPANESE GRAND PRIX 2023 ",
            "EventDate": "2023-09-24",
            "EventName": "Japanese Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-09-22 11:30:00+09:00",
            "Session1DateUtc": "2023-09-22 02:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-09-22 15:00:00+09:00",
            "Session2DateUtc": "2023-09-22 06:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-09-23 11:30:00+09:00",
            "Session3DateUtc": "2023-09-23 02:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-09-23 15:00:00+09:00",
            "Session4DateUtc": "2023-09-23 06:00:00",
            "Session5": "Race",
            "Session5Date": "2023-09-24 14:00:00+09:00",
            "Session5DateUtc": "2023-09-24 05:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 17,
            "Country": "Qatar",
            "Location": "Lusail",
            "OfficialEventName": "FORMULA 1 QATAR AIRWAYS QATAR GRAND PRIX 2023",
            "EventDate": "2023-10-08",
            "EventName": "Qatar Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-10-06 16:30:00+03:00",
            "Session1DateUtc": "2023-10-06 13:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-10-06 20:00:00+03:00",
            "Session2DateUtc": "2023-10-06 17:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-10-07 16:20:00+03:00",
            "Session3DateUtc": "2023-10-07 13:20:00",
            "Session4": "Sprint",
            "Session4Date": "2023-10-07 20:30:00+03:00",
            "Session4DateUtc": "2023-10-07 17:30:00",
            "Session5": "Race",
            "Session5Date": "2023-10-08 20:00:00+03:00",
            "Session5DateUtc": "2023-10-08 17:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 18,
            "Country": "United States",
            "Location": "Austin",
            "OfficialEventName": "FORMULA 1 LENOVO UNITED STATES GRAND PRIX 2023",
            "EventDate": "2023-10-22",
            "EventName": "United States Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-10-20 12:30:00-05:00",
            "Session1DateUtc": "2023-10-20 17:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-10-20 16:00:00-05:00",
            "Session2DateUtc": "2023-10-20 21:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-10-21 12:30:00-05:00",
            "Session3DateUtc": "2023-10-21 17:30:00",
            "Session4": "Sprint",
            "Session4Date": "2023-10-21 17:00:00-05:00",
            "Session4DateUtc": "2023-10-21 22:00:00",
            "Session5": "Race",
            "Session5Date": "2023-10-22 14:00:00-05:00",
            "Session5DateUtc": "2023-10-22 19:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 19,
            "Country": "Mexico",
            "Location": "Mexico City",
            "OfficialEventName": "FORMULA 1 GRAN PREMIO DE LA CIUDAD DE MÉXICO 2023",
            "EventDate": "2023-10-29",
            "EventName": "Mexico City Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-10-27 12:30:00-06:00",
            "Session1DateUtc": "2023-10-27 18:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-10-27 16:00:00-06:00",
            "Session2DateUtc": "2023-10-27 22:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-10-28 11:30:00-06:00",
            "Session3DateUtc": "2023-10-28 17:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-10-28 15:00:00-06:00",
            "Session4DateUtc": "2023-10-28 21:00:00",
            "Session5": "Race",
            "Session5Date": "2023-10-29 14:00:00-06:00",
            "Session5DateUtc": "2023-10-29 20:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 20,
            "Country": "Brazil",
            "Location": "São Paulo",
            "OfficialEventName": "FORMULA 1 ROLEX GRANDE PRÊMIO DE SÃO PAULO 2023",
            "EventDate": "2023-11-05",
            "EventName": "São Paulo Grand Prix",
            "EventFormat": "sprint_shootout",
            "Session1": "Practice 1",
            "Session1Date": "2023-11-03 11:30:00-03:00",
            "Session1DateUtc": "2023-11-03 14:30:00",
            "Session2": "Qualifying",
            "Session2Date": "2023-11-03 15:00:00-03:00",
            "Session2DateUtc": "2023-11-03 18:00:00",
            "Session3": "Sprint Shootout",
            "Session3Date": "2023-11-04 11:00:00-03:00",
            "Session3DateUtc": "2023-11-04 14:00:00",
            "Session4": "Sprint",
            "Session4Date": "2023-11-04 15:30:00-03:00",
            "Session4DateUtc": "2023-11-04 18:30:00",
            "Session5": "Race",
            "Session5Date": "2023-11-05 14:00:00-03:00",
            "Session5DateUtc": "2023-11-05 17:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 21,
            "Country": "United States",
            "Location": "Las Vegas",
            "OfficialEventName": "FORMULA 1 HEINEKEN SILVER LAS VEGAS GRAND PRIX 2023",
            "EventDate": "2023-11-18",
            "EventName": "Las Vegas Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-11-16 20:30:00-08:00",
            "Session1DateUtc": "2023-11-17 04:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-11-17 02:30:00-08:00",
            "Session2DateUtc": "2023-11-17 10:30:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-11-17 20:30:00-08:00",
            "Session3DateUtc": "2023-11-18 04:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-11-18 00:00:00-08:00",
            "Session4DateUtc": "2023-11-18 08:00:00",
            "Session5": "Race",
            "Session5Date": "2023-11-18 22:00:00-08:00",
            "Session5DateUtc": "2023-11-19 06:00:00",
            "F1ApiSupport": True,
        },
        {
            "RoundNumber": 22,
            "Country": "Abu Dhabi",
            "Location": "Yas Island",
            "OfficialEventName": "FORMULA 1 ETIHAD AIRWAYS ABU DHABI GRAND PRIX 2023 ",
            "EventDate": "2023-11-26",
            "EventName": "Abu Dhabi Grand Prix",
            "EventFormat": "conventional",
            "Session1": "Practice 1",
            "Session1Date": "2023-11-24 13:30:00+04:00",
            "Session1DateUtc": "2023-11-24 09:30:00",
            "Session2": "Practice 2",
            "Session2Date": "2023-11-24 17:00:00+04:00",
            "Session2DateUtc": "2023-11-24 13:00:00",
            "Session3": "Practice 3",
            "Session3Date": "2023-11-25 14:30:00+04:00",
            "Session3DateUtc": "2023-11-25 10:30:00",
            "Session4": "Qualifying",
            "Session4Date": "2023-11-25 18:00:00+04:00",
            "Session4DateUtc": "2023-11-25 14:00:00",
            "Session5": "Race",
            "Session5Date": "2023-11-26 17:00:00+04:00",
            "Session5DateUtc": "2023-11-26 13:00:00",
            "F1ApiSupport": True,
        },
    ]


# endregion schedule - good inputs

# region schedule - no or bad inputs


def test_get_schedule_bad_year_no_input():
    response = client.get("/schedule?year=")
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
    response = client.get(f"/schedule?year={MIN_SUPPORTED_YEAR - 1}")
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
    response = client.get(f"/schedule?year={MAX_SUPPORTED_YEAR + 1}")
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


# endregion schedule - no or bad inputs

# endregion schedule


# region standings

# region standings - good inputs


def test_get_standings():
    response = client.get("/standings")
    assert response.status_code == 200
    assert response.json() == {
        "season": 2023,
        "round": 22,
        "DriverStandings": [
            {
                "position": "1",
                "positionText": "1",
                "points": "575",
                "wins": "19",
                "Driver": {
                    "driverId": "max_verstappen",
                    "permanentNumber": "33",
                    "code": "VER",
                    "url": "http://en.wikipedia.org/wiki/Max_Verstappen",
                    "givenName": "Max",
                    "familyName": "Verstappen",
                    "dateOfBirth": "1997-09-30",
                    "nationality": "Dutch",
                },
                "Constructors": [
                    {
                        "constructorId": "red_bull",
                        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian",
                    }
                ],
            },
            {
                "position": "2",
                "positionText": "2",
                "points": "285",
                "wins": "2",
                "Driver": {
                    "driverId": "perez",
                    "permanentNumber": "11",
                    "code": "PER",
                    "url": "http://en.wikipedia.org/wiki/Sergio_P%C3%A9rez",
                    "givenName": "Sergio",
                    "familyName": "Pérez",
                    "dateOfBirth": "1990-01-26",
                    "nationality": "Mexican",
                },
                "Constructors": [
                    {
                        "constructorId": "red_bull",
                        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian",
                    }
                ],
            },
            {
                "position": "3",
                "positionText": "3",
                "points": "234",
                "wins": "0",
                "Driver": {
                    "driverId": "hamilton",
                    "permanentNumber": "44",
                    "code": "HAM",
                    "url": "http://en.wikipedia.org/wiki/Lewis_Hamilton",
                    "givenName": "Lewis",
                    "familyName": "Hamilton",
                    "dateOfBirth": "1985-01-07",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mercedes",
                        "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                        "name": "Mercedes",
                        "nationality": "German",
                    }
                ],
            },
            {
                "position": "4",
                "positionText": "4",
                "points": "206",
                "wins": "0",
                "Driver": {
                    "driverId": "alonso",
                    "permanentNumber": "14",
                    "code": "ALO",
                    "url": "http://en.wikipedia.org/wiki/Fernando_Alonso",
                    "givenName": "Fernando",
                    "familyName": "Alonso",
                    "dateOfBirth": "1981-07-29",
                    "nationality": "Spanish",
                },
                "Constructors": [
                    {
                        "constructorId": "aston_martin",
                        "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                        "name": "Aston Martin",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "5",
                "positionText": "5",
                "points": "206",
                "wins": "0",
                "Driver": {
                    "driverId": "leclerc",
                    "permanentNumber": "16",
                    "code": "LEC",
                    "url": "http://en.wikipedia.org/wiki/Charles_Leclerc",
                    "givenName": "Charles",
                    "familyName": "Leclerc",
                    "dateOfBirth": "1997-10-16",
                    "nationality": "Monegasque",
                },
                "Constructors": [
                    {
                        "constructorId": "ferrari",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                        "name": "Ferrari",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "6",
                "positionText": "6",
                "points": "205",
                "wins": "0",
                "Driver": {
                    "driverId": "norris",
                    "permanentNumber": "4",
                    "code": "NOR",
                    "url": "http://en.wikipedia.org/wiki/Lando_Norris",
                    "givenName": "Lando",
                    "familyName": "Norris",
                    "dateOfBirth": "1999-11-13",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mclaren",
                        "url": "http://en.wikipedia.org/wiki/McLaren",
                        "name": "McLaren",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "7",
                "positionText": "7",
                "points": "200",
                "wins": "1",
                "Driver": {
                    "driverId": "sainz",
                    "permanentNumber": "55",
                    "code": "SAI",
                    "url": "http://en.wikipedia.org/wiki/Carlos_Sainz_Jr.",
                    "givenName": "Carlos",
                    "familyName": "Sainz",
                    "dateOfBirth": "1994-09-01",
                    "nationality": "Spanish",
                },
                "Constructors": [
                    {
                        "constructorId": "ferrari",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                        "name": "Ferrari",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "8",
                "positionText": "8",
                "points": "175",
                "wins": "0",
                "Driver": {
                    "driverId": "russell",
                    "permanentNumber": "63",
                    "code": "RUS",
                    "url": "http://en.wikipedia.org/wiki/George_Russell_(racing_driver)",
                    "givenName": "George",
                    "familyName": "Russell",
                    "dateOfBirth": "1998-02-15",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mercedes",
                        "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                        "name": "Mercedes",
                        "nationality": "German",
                    }
                ],
            },
            {
                "position": "9",
                "positionText": "9",
                "points": "97",
                "wins": "0",
                "Driver": {
                    "driverId": "piastri",
                    "permanentNumber": "81",
                    "code": "PIA",
                    "url": "http://en.wikipedia.org/wiki/Oscar_Piastri",
                    "givenName": "Oscar",
                    "familyName": "Piastri",
                    "dateOfBirth": "2001-04-06",
                    "nationality": "Australian",
                },
                "Constructors": [
                    {
                        "constructorId": "mclaren",
                        "url": "http://en.wikipedia.org/wiki/McLaren",
                        "name": "McLaren",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "10",
                "positionText": "10",
                "points": "74",
                "wins": "0",
                "Driver": {
                    "driverId": "stroll",
                    "permanentNumber": "18",
                    "code": "STR",
                    "url": "http://en.wikipedia.org/wiki/Lance_Stroll",
                    "givenName": "Lance",
                    "familyName": "Stroll",
                    "dateOfBirth": "1998-10-29",
                    "nationality": "Canadian",
                },
                "Constructors": [
                    {
                        "constructorId": "aston_martin",
                        "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                        "name": "Aston Martin",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "11",
                "positionText": "11",
                "points": "62",
                "wins": "0",
                "Driver": {
                    "driverId": "gasly",
                    "permanentNumber": "10",
                    "code": "GAS",
                    "url": "http://en.wikipedia.org/wiki/Pierre_Gasly",
                    "givenName": "Pierre",
                    "familyName": "Gasly",
                    "dateOfBirth": "1996-02-07",
                    "nationality": "French",
                },
                "Constructors": [
                    {
                        "constructorId": "alpine",
                        "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                        "name": "Alpine F1 Team",
                        "nationality": "French",
                    }
                ],
            },
            {
                "position": "12",
                "positionText": "12",
                "points": "58",
                "wins": "0",
                "Driver": {
                    "driverId": "ocon",
                    "permanentNumber": "31",
                    "code": "OCO",
                    "url": "http://en.wikipedia.org/wiki/Esteban_Ocon",
                    "givenName": "Esteban",
                    "familyName": "Ocon",
                    "dateOfBirth": "1996-09-17",
                    "nationality": "French",
                },
                "Constructors": [
                    {
                        "constructorId": "alpine",
                        "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                        "name": "Alpine F1 Team",
                        "nationality": "French",
                    }
                ],
            },
            {
                "position": "13",
                "positionText": "13",
                "points": "27",
                "wins": "0",
                "Driver": {
                    "driverId": "albon",
                    "permanentNumber": "23",
                    "code": "ALB",
                    "url": "http://en.wikipedia.org/wiki/Alexander_Albon",
                    "givenName": "Alexander",
                    "familyName": "Albon",
                    "dateOfBirth": "1996-03-23",
                    "nationality": "Thai",
                },
                "Constructors": [
                    {
                        "constructorId": "williams",
                        "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                        "name": "Williams",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "14",
                "positionText": "14",
                "points": "17",
                "wins": "0",
                "Driver": {
                    "driverId": "tsunoda",
                    "permanentNumber": "22",
                    "code": "TSU",
                    "url": "http://en.wikipedia.org/wiki/Yuki_Tsunoda",
                    "givenName": "Yuki",
                    "familyName": "Tsunoda",
                    "dateOfBirth": "2000-05-11",
                    "nationality": "Japanese",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "15",
                "positionText": "15",
                "points": "10",
                "wins": "0",
                "Driver": {
                    "driverId": "bottas",
                    "permanentNumber": "77",
                    "code": "BOT",
                    "url": "http://en.wikipedia.org/wiki/Valtteri_Bottas",
                    "givenName": "Valtteri",
                    "familyName": "Bottas",
                    "dateOfBirth": "1989-08-28",
                    "nationality": "Finnish",
                },
                "Constructors": [
                    {
                        "constructorId": "alfa",
                        "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                        "name": "Alfa Romeo",
                        "nationality": "Swiss",
                    }
                ],
            },
            {
                "position": "16",
                "positionText": "16",
                "points": "9",
                "wins": "0",
                "Driver": {
                    "driverId": "hulkenberg",
                    "permanentNumber": "27",
                    "code": "HUL",
                    "url": "http://en.wikipedia.org/wiki/Nico_H%C3%BClkenberg",
                    "givenName": "Nico",
                    "familyName": "Hülkenberg",
                    "dateOfBirth": "1987-08-19",
                    "nationality": "German",
                },
                "Constructors": [
                    {
                        "constructorId": "haas",
                        "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                        "name": "Haas F1 Team",
                        "nationality": "American",
                    }
                ],
            },
            {
                "position": "17",
                "positionText": "17",
                "points": "6",
                "wins": "0",
                "Driver": {
                    "driverId": "ricciardo",
                    "permanentNumber": "3",
                    "code": "RIC",
                    "url": "http://en.wikipedia.org/wiki/Daniel_Ricciardo",
                    "givenName": "Daniel",
                    "familyName": "Ricciardo",
                    "dateOfBirth": "1989-07-01",
                    "nationality": "Australian",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "18",
                "positionText": "18",
                "points": "6",
                "wins": "0",
                "Driver": {
                    "driverId": "zhou",
                    "permanentNumber": "24",
                    "code": "ZHO",
                    "url": "http://en.wikipedia.org/wiki/Zhou_Guanyu",
                    "givenName": "Guanyu",
                    "familyName": "Zhou",
                    "dateOfBirth": "1999-05-30",
                    "nationality": "Chinese",
                },
                "Constructors": [
                    {
                        "constructorId": "alfa",
                        "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                        "name": "Alfa Romeo",
                        "nationality": "Swiss",
                    }
                ],
            },
            {
                "position": "19",
                "positionText": "19",
                "points": "3",
                "wins": "0",
                "Driver": {
                    "driverId": "kevin_magnussen",
                    "permanentNumber": "20",
                    "code": "MAG",
                    "url": "http://en.wikipedia.org/wiki/Kevin_Magnussen",
                    "givenName": "Kevin",
                    "familyName": "Magnussen",
                    "dateOfBirth": "1992-10-05",
                    "nationality": "Danish",
                },
                "Constructors": [
                    {
                        "constructorId": "haas",
                        "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                        "name": "Haas F1 Team",
                        "nationality": "American",
                    }
                ],
            },
            {
                "position": "20",
                "positionText": "20",
                "points": "2",
                "wins": "0",
                "Driver": {
                    "driverId": "lawson",
                    "permanentNumber": "40",
                    "code": "LAW",
                    "url": "http://en.wikipedia.org/wiki/Liam_Lawson",
                    "givenName": "Liam",
                    "familyName": "Lawson",
                    "dateOfBirth": "2002-02-11",
                    "nationality": "New Zealander",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "21",
                "positionText": "21",
                "points": "1",
                "wins": "0",
                "Driver": {
                    "driverId": "sargeant",
                    "permanentNumber": "2",
                    "code": "SAR",
                    "url": "http://en.wikipedia.org/wiki/Logan_Sargeant",
                    "givenName": "Logan",
                    "familyName": "Sargeant",
                    "dateOfBirth": "2000-12-31",
                    "nationality": "American",
                },
                "Constructors": [
                    {
                        "constructorId": "williams",
                        "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                        "name": "Williams",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "22",
                "positionText": "22",
                "points": "0",
                "wins": "0",
                "Driver": {
                    "driverId": "de_vries",
                    "permanentNumber": "21",
                    "code": "DEV",
                    "url": "http://en.wikipedia.org/wiki/Nyck_de_Vries",
                    "givenName": "Nyck",
                    "familyName": "de Vries",
                    "dateOfBirth": "1995-02-06",
                    "nationality": "Dutch",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
        ],
        "ConstructorStandings": [
            {
                "position": "1",
                "positionText": "1",
                "points": "860",
                "wins": "21",
                "Constructor": {
                    "constructorId": "red_bull",
                    "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                    "name": "Red Bull",
                    "nationality": "Austrian",
                },
            },
            {
                "position": "2",
                "positionText": "2",
                "points": "409",
                "wins": "0",
                "Constructor": {
                    "constructorId": "mercedes",
                    "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                    "name": "Mercedes",
                    "nationality": "German",
                },
            },
            {
                "position": "3",
                "positionText": "3",
                "points": "406",
                "wins": "1",
                "Constructor": {
                    "constructorId": "ferrari",
                    "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                    "name": "Ferrari",
                    "nationality": "Italian",
                },
            },
            {
                "position": "4",
                "positionText": "4",
                "points": "302",
                "wins": "0",
                "Constructor": {
                    "constructorId": "mclaren",
                    "url": "http://en.wikipedia.org/wiki/McLaren",
                    "name": "McLaren",
                    "nationality": "British",
                },
            },
            {
                "position": "5",
                "positionText": "5",
                "points": "280",
                "wins": "0",
                "Constructor": {
                    "constructorId": "aston_martin",
                    "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                    "name": "Aston Martin",
                    "nationality": "British",
                },
            },
            {
                "position": "6",
                "positionText": "6",
                "points": "120",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alpine",
                    "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                    "name": "Alpine F1 Team",
                    "nationality": "French",
                },
            },
            {
                "position": "7",
                "positionText": "7",
                "points": "28",
                "wins": "0",
                "Constructor": {
                    "constructorId": "williams",
                    "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                    "name": "Williams",
                    "nationality": "British",
                },
            },
            {
                "position": "8",
                "positionText": "8",
                "points": "25",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alphatauri",
                    "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                    "name": "AlphaTauri",
                    "nationality": "Italian",
                },
            },
            {
                "position": "9",
                "positionText": "9",
                "points": "16",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alfa",
                    "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                    "name": "Alfa Romeo",
                    "nationality": "Swiss",
                },
            },
            {
                "position": "10",
                "positionText": "10",
                "points": "12",
                "wins": "0",
                "Constructor": {
                    "constructorId": "haas",
                    "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                    "name": "Haas F1 Team",
                    "nationality": "American",
                },
            },
        ],
    }


def test_get_standings_good_year_only():
    response = client.get("/standings?year=2023")
    assert response.status_code == 200
    assert response.json() == {
        "season": 2023,
        "round": 22,
        "DriverStandings": [
            {
                "position": "1",
                "positionText": "1",
                "points": "575",
                "wins": "19",
                "Driver": {
                    "driverId": "max_verstappen",
                    "permanentNumber": "33",
                    "code": "VER",
                    "url": "http://en.wikipedia.org/wiki/Max_Verstappen",
                    "givenName": "Max",
                    "familyName": "Verstappen",
                    "dateOfBirth": "1997-09-30",
                    "nationality": "Dutch",
                },
                "Constructors": [
                    {
                        "constructorId": "red_bull",
                        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian",
                    }
                ],
            },
            {
                "position": "2",
                "positionText": "2",
                "points": "285",
                "wins": "2",
                "Driver": {
                    "driverId": "perez",
                    "permanentNumber": "11",
                    "code": "PER",
                    "url": "http://en.wikipedia.org/wiki/Sergio_P%C3%A9rez",
                    "givenName": "Sergio",
                    "familyName": "Pérez",
                    "dateOfBirth": "1990-01-26",
                    "nationality": "Mexican",
                },
                "Constructors": [
                    {
                        "constructorId": "red_bull",
                        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian",
                    }
                ],
            },
            {
                "position": "3",
                "positionText": "3",
                "points": "234",
                "wins": "0",
                "Driver": {
                    "driverId": "hamilton",
                    "permanentNumber": "44",
                    "code": "HAM",
                    "url": "http://en.wikipedia.org/wiki/Lewis_Hamilton",
                    "givenName": "Lewis",
                    "familyName": "Hamilton",
                    "dateOfBirth": "1985-01-07",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mercedes",
                        "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                        "name": "Mercedes",
                        "nationality": "German",
                    }
                ],
            },
            {
                "position": "4",
                "positionText": "4",
                "points": "206",
                "wins": "0",
                "Driver": {
                    "driverId": "alonso",
                    "permanentNumber": "14",
                    "code": "ALO",
                    "url": "http://en.wikipedia.org/wiki/Fernando_Alonso",
                    "givenName": "Fernando",
                    "familyName": "Alonso",
                    "dateOfBirth": "1981-07-29",
                    "nationality": "Spanish",
                },
                "Constructors": [
                    {
                        "constructorId": "aston_martin",
                        "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                        "name": "Aston Martin",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "5",
                "positionText": "5",
                "points": "206",
                "wins": "0",
                "Driver": {
                    "driverId": "leclerc",
                    "permanentNumber": "16",
                    "code": "LEC",
                    "url": "http://en.wikipedia.org/wiki/Charles_Leclerc",
                    "givenName": "Charles",
                    "familyName": "Leclerc",
                    "dateOfBirth": "1997-10-16",
                    "nationality": "Monegasque",
                },
                "Constructors": [
                    {
                        "constructorId": "ferrari",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                        "name": "Ferrari",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "6",
                "positionText": "6",
                "points": "205",
                "wins": "0",
                "Driver": {
                    "driverId": "norris",
                    "permanentNumber": "4",
                    "code": "NOR",
                    "url": "http://en.wikipedia.org/wiki/Lando_Norris",
                    "givenName": "Lando",
                    "familyName": "Norris",
                    "dateOfBirth": "1999-11-13",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mclaren",
                        "url": "http://en.wikipedia.org/wiki/McLaren",
                        "name": "McLaren",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "7",
                "positionText": "7",
                "points": "200",
                "wins": "1",
                "Driver": {
                    "driverId": "sainz",
                    "permanentNumber": "55",
                    "code": "SAI",
                    "url": "http://en.wikipedia.org/wiki/Carlos_Sainz_Jr.",
                    "givenName": "Carlos",
                    "familyName": "Sainz",
                    "dateOfBirth": "1994-09-01",
                    "nationality": "Spanish",
                },
                "Constructors": [
                    {
                        "constructorId": "ferrari",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                        "name": "Ferrari",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "8",
                "positionText": "8",
                "points": "175",
                "wins": "0",
                "Driver": {
                    "driverId": "russell",
                    "permanentNumber": "63",
                    "code": "RUS",
                    "url": "http://en.wikipedia.org/wiki/George_Russell_(racing_driver)",
                    "givenName": "George",
                    "familyName": "Russell",
                    "dateOfBirth": "1998-02-15",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mercedes",
                        "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                        "name": "Mercedes",
                        "nationality": "German",
                    }
                ],
            },
            {
                "position": "9",
                "positionText": "9",
                "points": "97",
                "wins": "0",
                "Driver": {
                    "driverId": "piastri",
                    "permanentNumber": "81",
                    "code": "PIA",
                    "url": "http://en.wikipedia.org/wiki/Oscar_Piastri",
                    "givenName": "Oscar",
                    "familyName": "Piastri",
                    "dateOfBirth": "2001-04-06",
                    "nationality": "Australian",
                },
                "Constructors": [
                    {
                        "constructorId": "mclaren",
                        "url": "http://en.wikipedia.org/wiki/McLaren",
                        "name": "McLaren",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "10",
                "positionText": "10",
                "points": "74",
                "wins": "0",
                "Driver": {
                    "driverId": "stroll",
                    "permanentNumber": "18",
                    "code": "STR",
                    "url": "http://en.wikipedia.org/wiki/Lance_Stroll",
                    "givenName": "Lance",
                    "familyName": "Stroll",
                    "dateOfBirth": "1998-10-29",
                    "nationality": "Canadian",
                },
                "Constructors": [
                    {
                        "constructorId": "aston_martin",
                        "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                        "name": "Aston Martin",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "11",
                "positionText": "11",
                "points": "62",
                "wins": "0",
                "Driver": {
                    "driverId": "gasly",
                    "permanentNumber": "10",
                    "code": "GAS",
                    "url": "http://en.wikipedia.org/wiki/Pierre_Gasly",
                    "givenName": "Pierre",
                    "familyName": "Gasly",
                    "dateOfBirth": "1996-02-07",
                    "nationality": "French",
                },
                "Constructors": [
                    {
                        "constructorId": "alpine",
                        "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                        "name": "Alpine F1 Team",
                        "nationality": "French",
                    }
                ],
            },
            {
                "position": "12",
                "positionText": "12",
                "points": "58",
                "wins": "0",
                "Driver": {
                    "driverId": "ocon",
                    "permanentNumber": "31",
                    "code": "OCO",
                    "url": "http://en.wikipedia.org/wiki/Esteban_Ocon",
                    "givenName": "Esteban",
                    "familyName": "Ocon",
                    "dateOfBirth": "1996-09-17",
                    "nationality": "French",
                },
                "Constructors": [
                    {
                        "constructorId": "alpine",
                        "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                        "name": "Alpine F1 Team",
                        "nationality": "French",
                    }
                ],
            },
            {
                "position": "13",
                "positionText": "13",
                "points": "27",
                "wins": "0",
                "Driver": {
                    "driverId": "albon",
                    "permanentNumber": "23",
                    "code": "ALB",
                    "url": "http://en.wikipedia.org/wiki/Alexander_Albon",
                    "givenName": "Alexander",
                    "familyName": "Albon",
                    "dateOfBirth": "1996-03-23",
                    "nationality": "Thai",
                },
                "Constructors": [
                    {
                        "constructorId": "williams",
                        "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                        "name": "Williams",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "14",
                "positionText": "14",
                "points": "17",
                "wins": "0",
                "Driver": {
                    "driverId": "tsunoda",
                    "permanentNumber": "22",
                    "code": "TSU",
                    "url": "http://en.wikipedia.org/wiki/Yuki_Tsunoda",
                    "givenName": "Yuki",
                    "familyName": "Tsunoda",
                    "dateOfBirth": "2000-05-11",
                    "nationality": "Japanese",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "15",
                "positionText": "15",
                "points": "10",
                "wins": "0",
                "Driver": {
                    "driverId": "bottas",
                    "permanentNumber": "77",
                    "code": "BOT",
                    "url": "http://en.wikipedia.org/wiki/Valtteri_Bottas",
                    "givenName": "Valtteri",
                    "familyName": "Bottas",
                    "dateOfBirth": "1989-08-28",
                    "nationality": "Finnish",
                },
                "Constructors": [
                    {
                        "constructorId": "alfa",
                        "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                        "name": "Alfa Romeo",
                        "nationality": "Swiss",
                    }
                ],
            },
            {
                "position": "16",
                "positionText": "16",
                "points": "9",
                "wins": "0",
                "Driver": {
                    "driverId": "hulkenberg",
                    "permanentNumber": "27",
                    "code": "HUL",
                    "url": "http://en.wikipedia.org/wiki/Nico_H%C3%BClkenberg",
                    "givenName": "Nico",
                    "familyName": "Hülkenberg",
                    "dateOfBirth": "1987-08-19",
                    "nationality": "German",
                },
                "Constructors": [
                    {
                        "constructorId": "haas",
                        "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                        "name": "Haas F1 Team",
                        "nationality": "American",
                    }
                ],
            },
            {
                "position": "17",
                "positionText": "17",
                "points": "6",
                "wins": "0",
                "Driver": {
                    "driverId": "ricciardo",
                    "permanentNumber": "3",
                    "code": "RIC",
                    "url": "http://en.wikipedia.org/wiki/Daniel_Ricciardo",
                    "givenName": "Daniel",
                    "familyName": "Ricciardo",
                    "dateOfBirth": "1989-07-01",
                    "nationality": "Australian",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "18",
                "positionText": "18",
                "points": "6",
                "wins": "0",
                "Driver": {
                    "driverId": "zhou",
                    "permanentNumber": "24",
                    "code": "ZHO",
                    "url": "http://en.wikipedia.org/wiki/Zhou_Guanyu",
                    "givenName": "Guanyu",
                    "familyName": "Zhou",
                    "dateOfBirth": "1999-05-30",
                    "nationality": "Chinese",
                },
                "Constructors": [
                    {
                        "constructorId": "alfa",
                        "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                        "name": "Alfa Romeo",
                        "nationality": "Swiss",
                    }
                ],
            },
            {
                "position": "19",
                "positionText": "19",
                "points": "3",
                "wins": "0",
                "Driver": {
                    "driverId": "kevin_magnussen",
                    "permanentNumber": "20",
                    "code": "MAG",
                    "url": "http://en.wikipedia.org/wiki/Kevin_Magnussen",
                    "givenName": "Kevin",
                    "familyName": "Magnussen",
                    "dateOfBirth": "1992-10-05",
                    "nationality": "Danish",
                },
                "Constructors": [
                    {
                        "constructorId": "haas",
                        "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                        "name": "Haas F1 Team",
                        "nationality": "American",
                    }
                ],
            },
            {
                "position": "20",
                "positionText": "20",
                "points": "2",
                "wins": "0",
                "Driver": {
                    "driverId": "lawson",
                    "permanentNumber": "40",
                    "code": "LAW",
                    "url": "http://en.wikipedia.org/wiki/Liam_Lawson",
                    "givenName": "Liam",
                    "familyName": "Lawson",
                    "dateOfBirth": "2002-02-11",
                    "nationality": "New Zealander",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "21",
                "positionText": "21",
                "points": "1",
                "wins": "0",
                "Driver": {
                    "driverId": "sargeant",
                    "permanentNumber": "2",
                    "code": "SAR",
                    "url": "http://en.wikipedia.org/wiki/Logan_Sargeant",
                    "givenName": "Logan",
                    "familyName": "Sargeant",
                    "dateOfBirth": "2000-12-31",
                    "nationality": "American",
                },
                "Constructors": [
                    {
                        "constructorId": "williams",
                        "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                        "name": "Williams",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "22",
                "positionText": "22",
                "points": "0",
                "wins": "0",
                "Driver": {
                    "driverId": "de_vries",
                    "permanentNumber": "21",
                    "code": "DEV",
                    "url": "http://en.wikipedia.org/wiki/Nyck_de_Vries",
                    "givenName": "Nyck",
                    "familyName": "de Vries",
                    "dateOfBirth": "1995-02-06",
                    "nationality": "Dutch",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
        ],
        "ConstructorStandings": [
            {
                "position": "1",
                "positionText": "1",
                "points": "860",
                "wins": "21",
                "Constructor": {
                    "constructorId": "red_bull",
                    "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                    "name": "Red Bull",
                    "nationality": "Austrian",
                },
            },
            {
                "position": "2",
                "positionText": "2",
                "points": "409",
                "wins": "0",
                "Constructor": {
                    "constructorId": "mercedes",
                    "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                    "name": "Mercedes",
                    "nationality": "German",
                },
            },
            {
                "position": "3",
                "positionText": "3",
                "points": "406",
                "wins": "1",
                "Constructor": {
                    "constructorId": "ferrari",
                    "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                    "name": "Ferrari",
                    "nationality": "Italian",
                },
            },
            {
                "position": "4",
                "positionText": "4",
                "points": "302",
                "wins": "0",
                "Constructor": {
                    "constructorId": "mclaren",
                    "url": "http://en.wikipedia.org/wiki/McLaren",
                    "name": "McLaren",
                    "nationality": "British",
                },
            },
            {
                "position": "5",
                "positionText": "5",
                "points": "280",
                "wins": "0",
                "Constructor": {
                    "constructorId": "aston_martin",
                    "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                    "name": "Aston Martin",
                    "nationality": "British",
                },
            },
            {
                "position": "6",
                "positionText": "6",
                "points": "120",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alpine",
                    "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                    "name": "Alpine F1 Team",
                    "nationality": "French",
                },
            },
            {
                "position": "7",
                "positionText": "7",
                "points": "28",
                "wins": "0",
                "Constructor": {
                    "constructorId": "williams",
                    "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                    "name": "Williams",
                    "nationality": "British",
                },
            },
            {
                "position": "8",
                "positionText": "8",
                "points": "25",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alphatauri",
                    "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                    "name": "AlphaTauri",
                    "nationality": "Italian",
                },
            },
            {
                "position": "9",
                "positionText": "9",
                "points": "16",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alfa",
                    "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                    "name": "Alfa Romeo",
                    "nationality": "Swiss",
                },
            },
            {
                "position": "10",
                "positionText": "10",
                "points": "12",
                "wins": "0",
                "Constructor": {
                    "constructorId": "haas",
                    "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                    "name": "Haas F1 Team",
                    "nationality": "American",
                },
            },
        ],
    }


def test_get_standings_good_year_and_round():
    response = client.get("/standings?year=2023&round=5")
    assert response.status_code == 200
    assert response.json() == {
        "season": 2023,
        "round": 5,
        "DriverStandings": [
            {
                "position": "1",
                "positionText": "1",
                "points": "119",
                "wins": "3",
                "Driver": {
                    "driverId": "max_verstappen",
                    "permanentNumber": "33",
                    "code": "VER",
                    "url": "http://en.wikipedia.org/wiki/Max_Verstappen",
                    "givenName": "Max",
                    "familyName": "Verstappen",
                    "dateOfBirth": "1997-09-30",
                    "nationality": "Dutch",
                },
                "Constructors": [
                    {
                        "constructorId": "red_bull",
                        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian",
                    }
                ],
            },
            {
                "position": "2",
                "positionText": "2",
                "points": "105",
                "wins": "2",
                "Driver": {
                    "driverId": "perez",
                    "permanentNumber": "11",
                    "code": "PER",
                    "url": "http://en.wikipedia.org/wiki/Sergio_P%C3%A9rez",
                    "givenName": "Sergio",
                    "familyName": "Pérez",
                    "dateOfBirth": "1990-01-26",
                    "nationality": "Mexican",
                },
                "Constructors": [
                    {
                        "constructorId": "red_bull",
                        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                        "name": "Red Bull",
                        "nationality": "Austrian",
                    }
                ],
            },
            {
                "position": "3",
                "positionText": "3",
                "points": "75",
                "wins": "0",
                "Driver": {
                    "driverId": "alonso",
                    "permanentNumber": "14",
                    "code": "ALO",
                    "url": "http://en.wikipedia.org/wiki/Fernando_Alonso",
                    "givenName": "Fernando",
                    "familyName": "Alonso",
                    "dateOfBirth": "1981-07-29",
                    "nationality": "Spanish",
                },
                "Constructors": [
                    {
                        "constructorId": "aston_martin",
                        "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                        "name": "Aston Martin",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "4",
                "positionText": "4",
                "points": "56",
                "wins": "0",
                "Driver": {
                    "driverId": "hamilton",
                    "permanentNumber": "44",
                    "code": "HAM",
                    "url": "http://en.wikipedia.org/wiki/Lewis_Hamilton",
                    "givenName": "Lewis",
                    "familyName": "Hamilton",
                    "dateOfBirth": "1985-01-07",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mercedes",
                        "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                        "name": "Mercedes",
                        "nationality": "German",
                    }
                ],
            },
            {
                "position": "5",
                "positionText": "5",
                "points": "44",
                "wins": "0",
                "Driver": {
                    "driverId": "sainz",
                    "permanentNumber": "55",
                    "code": "SAI",
                    "url": "http://en.wikipedia.org/wiki/Carlos_Sainz_Jr.",
                    "givenName": "Carlos",
                    "familyName": "Sainz",
                    "dateOfBirth": "1994-09-01",
                    "nationality": "Spanish",
                },
                "Constructors": [
                    {
                        "constructorId": "ferrari",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                        "name": "Ferrari",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "6",
                "positionText": "6",
                "points": "40",
                "wins": "0",
                "Driver": {
                    "driverId": "russell",
                    "permanentNumber": "63",
                    "code": "RUS",
                    "url": "http://en.wikipedia.org/wiki/George_Russell_(racing_driver)",
                    "givenName": "George",
                    "familyName": "Russell",
                    "dateOfBirth": "1998-02-15",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mercedes",
                        "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                        "name": "Mercedes",
                        "nationality": "German",
                    }
                ],
            },
            {
                "position": "7",
                "positionText": "7",
                "points": "34",
                "wins": "0",
                "Driver": {
                    "driverId": "leclerc",
                    "permanentNumber": "16",
                    "code": "LEC",
                    "url": "http://en.wikipedia.org/wiki/Charles_Leclerc",
                    "givenName": "Charles",
                    "familyName": "Leclerc",
                    "dateOfBirth": "1997-10-16",
                    "nationality": "Monegasque",
                },
                "Constructors": [
                    {
                        "constructorId": "ferrari",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                        "name": "Ferrari",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "8",
                "positionText": "8",
                "points": "27",
                "wins": "0",
                "Driver": {
                    "driverId": "stroll",
                    "permanentNumber": "18",
                    "code": "STR",
                    "url": "http://en.wikipedia.org/wiki/Lance_Stroll",
                    "givenName": "Lance",
                    "familyName": "Stroll",
                    "dateOfBirth": "1998-10-29",
                    "nationality": "Canadian",
                },
                "Constructors": [
                    {
                        "constructorId": "aston_martin",
                        "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                        "name": "Aston Martin",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "9",
                "positionText": "9",
                "points": "10",
                "wins": "0",
                "Driver": {
                    "driverId": "norris",
                    "permanentNumber": "4",
                    "code": "NOR",
                    "url": "http://en.wikipedia.org/wiki/Lando_Norris",
                    "givenName": "Lando",
                    "familyName": "Norris",
                    "dateOfBirth": "1999-11-13",
                    "nationality": "British",
                },
                "Constructors": [
                    {
                        "constructorId": "mclaren",
                        "url": "http://en.wikipedia.org/wiki/McLaren",
                        "name": "McLaren",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "10",
                "positionText": "10",
                "points": "8",
                "wins": "0",
                "Driver": {
                    "driverId": "gasly",
                    "permanentNumber": "10",
                    "code": "GAS",
                    "url": "http://en.wikipedia.org/wiki/Pierre_Gasly",
                    "givenName": "Pierre",
                    "familyName": "Gasly",
                    "dateOfBirth": "1996-02-07",
                    "nationality": "French",
                },
                "Constructors": [
                    {
                        "constructorId": "alpine",
                        "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                        "name": "Alpine F1 Team",
                        "nationality": "French",
                    }
                ],
            },
            {
                "position": "11",
                "positionText": "11",
                "points": "6",
                "wins": "0",
                "Driver": {
                    "driverId": "hulkenberg",
                    "permanentNumber": "27",
                    "code": "HUL",
                    "url": "http://en.wikipedia.org/wiki/Nico_H%C3%BClkenberg",
                    "givenName": "Nico",
                    "familyName": "Hülkenberg",
                    "dateOfBirth": "1987-08-19",
                    "nationality": "German",
                },
                "Constructors": [
                    {
                        "constructorId": "haas",
                        "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                        "name": "Haas F1 Team",
                        "nationality": "American",
                    }
                ],
            },
            {
                "position": "12",
                "positionText": "12",
                "points": "6",
                "wins": "0",
                "Driver": {
                    "driverId": "ocon",
                    "permanentNumber": "31",
                    "code": "OCO",
                    "url": "http://en.wikipedia.org/wiki/Esteban_Ocon",
                    "givenName": "Esteban",
                    "familyName": "Ocon",
                    "dateOfBirth": "1996-09-17",
                    "nationality": "French",
                },
                "Constructors": [
                    {
                        "constructorId": "alpine",
                        "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                        "name": "Alpine F1 Team",
                        "nationality": "French",
                    }
                ],
            },
            {
                "position": "13",
                "positionText": "13",
                "points": "4",
                "wins": "0",
                "Driver": {
                    "driverId": "bottas",
                    "permanentNumber": "77",
                    "code": "BOT",
                    "url": "http://en.wikipedia.org/wiki/Valtteri_Bottas",
                    "givenName": "Valtteri",
                    "familyName": "Bottas",
                    "dateOfBirth": "1989-08-28",
                    "nationality": "Finnish",
                },
                "Constructors": [
                    {
                        "constructorId": "alfa",
                        "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                        "name": "Alfa Romeo",
                        "nationality": "Swiss",
                    }
                ],
            },
            {
                "position": "14",
                "positionText": "14",
                "points": "4",
                "wins": "0",
                "Driver": {
                    "driverId": "piastri",
                    "permanentNumber": "81",
                    "code": "PIA",
                    "url": "http://en.wikipedia.org/wiki/Oscar_Piastri",
                    "givenName": "Oscar",
                    "familyName": "Piastri",
                    "dateOfBirth": "2001-04-06",
                    "nationality": "Australian",
                },
                "Constructors": [
                    {
                        "constructorId": "mclaren",
                        "url": "http://en.wikipedia.org/wiki/McLaren",
                        "name": "McLaren",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "15",
                "positionText": "15",
                "points": "2",
                "wins": "0",
                "Driver": {
                    "driverId": "zhou",
                    "permanentNumber": "24",
                    "code": "ZHO",
                    "url": "http://en.wikipedia.org/wiki/Zhou_Guanyu",
                    "givenName": "Guanyu",
                    "familyName": "Zhou",
                    "dateOfBirth": "1999-05-30",
                    "nationality": "Chinese",
                },
                "Constructors": [
                    {
                        "constructorId": "alfa",
                        "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                        "name": "Alfa Romeo",
                        "nationality": "Swiss",
                    }
                ],
            },
            {
                "position": "16",
                "positionText": "16",
                "points": "2",
                "wins": "0",
                "Driver": {
                    "driverId": "tsunoda",
                    "permanentNumber": "22",
                    "code": "TSU",
                    "url": "http://en.wikipedia.org/wiki/Yuki_Tsunoda",
                    "givenName": "Yuki",
                    "familyName": "Tsunoda",
                    "dateOfBirth": "2000-05-11",
                    "nationality": "Japanese",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
            {
                "position": "17",
                "positionText": "17",
                "points": "2",
                "wins": "0",
                "Driver": {
                    "driverId": "kevin_magnussen",
                    "permanentNumber": "20",
                    "code": "MAG",
                    "url": "http://en.wikipedia.org/wiki/Kevin_Magnussen",
                    "givenName": "Kevin",
                    "familyName": "Magnussen",
                    "dateOfBirth": "1992-10-05",
                    "nationality": "Danish",
                },
                "Constructors": [
                    {
                        "constructorId": "haas",
                        "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                        "name": "Haas F1 Team",
                        "nationality": "American",
                    }
                ],
            },
            {
                "position": "18",
                "positionText": "18",
                "points": "1",
                "wins": "0",
                "Driver": {
                    "driverId": "albon",
                    "permanentNumber": "23",
                    "code": "ALB",
                    "url": "http://en.wikipedia.org/wiki/Alexander_Albon",
                    "givenName": "Alexander",
                    "familyName": "Albon",
                    "dateOfBirth": "1996-03-23",
                    "nationality": "Thai",
                },
                "Constructors": [
                    {
                        "constructorId": "williams",
                        "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                        "name": "Williams",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "19",
                "positionText": "19",
                "points": "0",
                "wins": "0",
                "Driver": {
                    "driverId": "sargeant",
                    "permanentNumber": "2",
                    "code": "SAR",
                    "url": "http://en.wikipedia.org/wiki/Logan_Sargeant",
                    "givenName": "Logan",
                    "familyName": "Sargeant",
                    "dateOfBirth": "2000-12-31",
                    "nationality": "American",
                },
                "Constructors": [
                    {
                        "constructorId": "williams",
                        "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                        "name": "Williams",
                        "nationality": "British",
                    }
                ],
            },
            {
                "position": "20",
                "positionText": "20",
                "points": "0",
                "wins": "0",
                "Driver": {
                    "driverId": "de_vries",
                    "permanentNumber": "21",
                    "code": "DEV",
                    "url": "http://en.wikipedia.org/wiki/Nyck_de_Vries",
                    "givenName": "Nyck",
                    "familyName": "de Vries",
                    "dateOfBirth": "1995-02-06",
                    "nationality": "Dutch",
                },
                "Constructors": [
                    {
                        "constructorId": "alphatauri",
                        "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                        "name": "AlphaTauri",
                        "nationality": "Italian",
                    }
                ],
            },
        ],
        "ConstructorStandings": [
            {
                "position": "1",
                "positionText": "1",
                "points": "224",
                "wins": "5",
                "Constructor": {
                    "constructorId": "red_bull",
                    "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
                    "name": "Red Bull",
                    "nationality": "Austrian",
                },
            },
            {
                "position": "2",
                "positionText": "2",
                "points": "102",
                "wins": "0",
                "Constructor": {
                    "constructorId": "aston_martin",
                    "url": "http://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
                    "name": "Aston Martin",
                    "nationality": "British",
                },
            },
            {
                "position": "3",
                "positionText": "3",
                "points": "96",
                "wins": "0",
                "Constructor": {
                    "constructorId": "mercedes",
                    "url": "http://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                    "name": "Mercedes",
                    "nationality": "German",
                },
            },
            {
                "position": "4",
                "positionText": "4",
                "points": "78",
                "wins": "0",
                "Constructor": {
                    "constructorId": "ferrari",
                    "url": "http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                    "name": "Ferrari",
                    "nationality": "Italian",
                },
            },
            {
                "position": "5",
                "positionText": "5",
                "points": "14",
                "wins": "0",
                "Constructor": {
                    "constructorId": "mclaren",
                    "url": "http://en.wikipedia.org/wiki/McLaren",
                    "name": "McLaren",
                    "nationality": "British",
                },
            },
            {
                "position": "6",
                "positionText": "6",
                "points": "14",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alpine",
                    "url": "http://en.wikipedia.org/wiki/Alpine_F1_Team",
                    "name": "Alpine F1 Team",
                    "nationality": "French",
                },
            },
            {
                "position": "7",
                "positionText": "7",
                "points": "8",
                "wins": "0",
                "Constructor": {
                    "constructorId": "haas",
                    "url": "http://en.wikipedia.org/wiki/Haas_F1_Team",
                    "name": "Haas F1 Team",
                    "nationality": "American",
                },
            },
            {
                "position": "8",
                "positionText": "8",
                "points": "6",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alfa",
                    "url": "http://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
                    "name": "Alfa Romeo",
                    "nationality": "Swiss",
                },
            },
            {
                "position": "9",
                "positionText": "9",
                "points": "2",
                "wins": "0",
                "Constructor": {
                    "constructorId": "alphatauri",
                    "url": "http://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
                    "name": "AlphaTauri",
                    "nationality": "Italian",
                },
            },
            {
                "position": "10",
                "positionText": "10",
                "points": "1",
                "wins": "0",
                "Constructor": {
                    "constructorId": "williams",
                    "url": "http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering",
                    "name": "Williams",
                    "nationality": "British",
                },
            },
        ],
    }


# endregion standings - good inputs

# region standings - no inputs


def test_get_standings_bad_year_only_no_input():
    response = client.get("/standings?year=")
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


def test_get_standings_bad_round_only_no_input():
    response = client.get("/standings?round=")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["query", "round"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "",
                "url": "https://errors.pydantic.dev/2.5/v/int_parsing",
            }
        ]
    }


def test_get_standings_good_round_bad_year_no_input():
    response = client.get("/standings?round=3")
    assert response.status_code == 400
    assert response.json() == {
        "detail": 'Bad request. Must provide the "year" parameter.'
    }


def test_get_standings_bad_year_and_round_no_input():
    response = client.get("/standings?year=&round=")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["query", "year"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "",
                "url": "https://errors.pydantic.dev/2.5/v/int_parsing",
            },
            {
                "type": "int_parsing",
                "loc": ["query", "round"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "",
                "url": "https://errors.pydantic.dev/2.5/v/int_parsing",
            },
        ]
    }


# endregion standings - no inputs

# region standings - bad inputs


def test_get_standings_bad_year_only_lower_limit():
    response = client.get(f"/standings?year={MIN_SUPPORTED_YEAR - 1}")
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


def test_get_standings_bad_year_only_upper_limit():
    response = client.get(f"/standings?year={MAX_SUPPORTED_YEAR + 1}")
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


def test_get_standings_bad_round_only_lower_limit():
    response = client.get(f"/standings?round={MIN_SUPPORTED_ROUND - 1}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be greater than or equal to 1",
                "input": "0",
                "ctx": {"ge": 1},
                "url": "https://errors.pydantic.dev/2.5/v/greater_than_equal",
            }
        ]
    }


def test_get_standings_bad_round_only_upper_limit():
    response = client.get(f"/standings?round={MAX_SUPPORTED_ROUND + 1}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "less_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be less than or equal to 30",
                "input": "31",
                "ctx": {"le": 30},
                "url": "https://errors.pydantic.dev/2.5/v/less_than_equal",
            }
        ]
    }


def test_get_standings_good_year_bad_round_lower_limit():
    response = client.get(f"/standings?year=2023&round={MIN_SUPPORTED_ROUND - 1}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be greater than or equal to 1",
                "input": "0",
                "ctx": {"ge": 1},
                "url": "https://errors.pydantic.dev/2.5/v/greater_than_equal",
            }
        ]
    }


def test_get_standings_good_year_bad_round_upper_limit():
    response = client.get(f"/standings?year=2023&round={MAX_SUPPORTED_ROUND + 1}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "less_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be less than or equal to 30",
                "input": "31",
                "ctx": {"le": 30},
                "url": "https://errors.pydantic.dev/2.5/v/less_than_equal",
            }
        ]
    }


def test_get_standings_good_round_bad_year_lower_limit():
    response = client.get(f"/standings?year={MIN_SUPPORTED_YEAR - 1}&round=2")
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


def test_get_standings_good_round_bad_year_upper_limit():
    response = client.get(f"/standings?year={MAX_SUPPORTED_YEAR + 1}&round=2")
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


def test_get_standings_bad_year_and_round_lower_limit():
    response = client.get(
        f"/standings?year={MIN_SUPPORTED_YEAR - 1}&round={MIN_SUPPORTED_ROUND - 1}"
    )
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
            },
            {
                "type": "greater_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be greater than or equal to 1",
                "input": "0",
                "ctx": {"ge": 1},
                "url": "https://errors.pydantic.dev/2.5/v/greater_than_equal",
            },
        ]
    }


def test_get_standings_bad_year_and_round_upper_limit():
    response = client.get(
        f"/standings?year={MAX_SUPPORTED_YEAR + 1}&round={MAX_SUPPORTED_ROUND + 1}"
    )
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
            },
            {
                "type": "less_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be less than or equal to 30",
                "input": "31",
                "ctx": {"le": 30},
                "url": "https://errors.pydantic.dev/2.5/v/less_than_equal",
            },
        ]
    }


def test_get_standings_bad_year_lower_limit_round_upper_limit():
    response = client.get(
        f"/standings?year={MIN_SUPPORTED_YEAR - 1}&round={MAX_SUPPORTED_ROUND + 1}"
    )
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
            },
            {
                "type": "less_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be less than or equal to 30",
                "input": "31",
                "ctx": {"le": 30},
                "url": "https://errors.pydantic.dev/2.5/v/less_than_equal",
            },
        ]
    }


def test_get_standings_bad_year_upper_limit_round_lower_limit():
    response = client.get(
        f"/standings?year={MAX_SUPPORTED_YEAR + 1}&round={MIN_SUPPORTED_ROUND - 1}"
    )
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
            },
            {
                "type": "greater_than_equal",
                "loc": ["query", "round"],
                "msg": "Input should be greater than or equal to 1",
                "input": "0",
                "ctx": {"ge": 1},
                "url": "https://errors.pydantic.dev/2.5/v/greater_than_equal",
            },
        ]
    }


# endregion standings - bad inputs

# endregion standings
