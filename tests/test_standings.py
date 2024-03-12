# External
from fastapi import status
from fastapi.testclient import TestClient

# Project
from app.main import app


client = TestClient(app)


# region good inputs


def test_get_standings():
    response = client.get("/standings")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["season"] == 2024
    assert response.json()["round"] == 2
    assert response.json()["DriverStandings"][0] == {
        "position": "1",
        "positionText": "1",
        "points": "51",
        "wins": "2",
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
    }
    assert response.json()["ConstructorStandings"][0] == {
        "position": "1",
        "positionText": "1",
        "points": "87",
        "wins": "2",
        "Constructor": {
            "constructorId": "red_bull",
            "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
            "name": "Red Bull",
            "nationality": "Austrian",
        },
    }


def test_get_standings_good_year_only():
    response = client.get("/standings?year=2023")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["season"] == 2023
    assert response.json()["round"] == 22
    assert response.json()["DriverStandings"][0] == {
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
    }
    assert response.json()["ConstructorStandings"][0] == {
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
    }


def test_get_standings_good_year_and_round():
    response = client.get("/standings?year=2023&round=5")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["season"] == 2023
    assert response.json()["round"] == 5
    assert response.json()["DriverStandings"][0] == {
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
    }
    assert response.json()["ConstructorStandings"][0] == {
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
    }


# endregion good inputs

# region no inputs


def test_get_standings_good_round_bad_year_no_input():
    response = client.get("/standings?round=3")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": 'Bad request. Must provide the "year" parameter.'}


# endregion no inputs
