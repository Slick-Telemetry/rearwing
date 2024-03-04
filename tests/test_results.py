# External
from fastapi import status
from fastapi.testclient import TestClient

# Project
from app.main import app


client = TestClient(app)


# region good inputs


def test_get_results():
    response = client.get("/results/2023/5")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == {
        "DriverNumber": "1",
        "BroadcastName": "M VERSTAPPEN",
        "Abbreviation": "VER",
        "DriverId": "max_verstappen",
        "TeamName": "Red Bull Racing",
        "TeamColor": "3671C6",
        "TeamId": "red_bull",
        "FirstName": "Max",
        "LastName": "Verstappen",
        "FullName": "Max Verstappen",
        "HeadshotUrl": "https://www.formula1.com/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/1col/image.png",
        "CountryCode": "NED",
        "Position": 1,
        "ClassifiedPosition": "1",
        "GridPosition": 9,
        "Q1": None,
        "Q2": None,
        "Q3": None,
        "Time": 5258241,
        "Status": "Finished",
        "Points": 26,
    }


def test_get_results_with_session():
    response = client.get("/results/2023/5?session=4")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == {
        "DriverNumber": "11",
        "BroadcastName": "S PEREZ",
        "Abbreviation": "PER",
        "DriverId": "perez",
        "TeamName": "Red Bull Racing",
        "TeamColor": "3671C6",
        "TeamId": "red_bull",
        "FirstName": "Sergio",
        "LastName": "Perez",
        "FullName": "Sergio Perez",
        "HeadshotUrl": "https://www.formula1.com/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png.transform/1col/image.png",
        "CountryCode": "MEX",
        "Position": 1,
        "ClassifiedPosition": "",
        "GridPosition": None,
        "Q1": 87713,
        "Q2": 87328,
        "Q3": 86841,
        "Time": None,
        "Status": "",
        "Points": None,
    }


# endregion good inputs

# region bad inputs


def test_get_results_bad_round_invalid():
    response = client.get("/results/2023/25?session=2")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Bad Request. Invalid round: 25"}


# endregion bad inputs
