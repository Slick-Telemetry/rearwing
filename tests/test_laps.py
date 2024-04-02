# External
from fastapi import status

# App
from . import client_with_auth


# region good inputs


def test_get_laps():
    response = client_with_auth.get("/laps/2023/5")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == {
        "Time": 3868310,
        "Driver": "VER",
        "DriverNumber": "1",
        "LapTime": 101724,
        "LapNumber": 1.0,
        "Stint": 1.0,
        "PitOutTime": None,
        "PitInTime": None,
        "Sector1Time": None,
        "Sector2Time": 36216,
        "Sector3Time": 26263,
        "Sector1SessionTime": None,
        "Sector2SessionTime": 3842065,
        "Sector3SessionTime": 3868409,
        "SpeedI1": 212.0,
        "SpeedI2": 186.0,
        "SpeedFL": 274.0,
        "SpeedST": 306.0,
        "IsPersonalBest": False,
        "Compound": "HARD",
        "TyreLife": 1.0,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 3766300,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": 9.0,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }


def test_get_laps_with_session_only():
    response = client_with_auth.get("/laps/2023/5?session=4")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == {
        "Time": 1098400,
        "Driver": "PER",
        "DriverNumber": "11",
        "LapTime": None,
        "LapNumber": 1.0,
        "Stint": 1.0,
        "PitOutTime": 979230,
        "PitInTime": None,
        "Sector1Time": None,
        "Sector2Time": 46024,
        "Sector3Time": 33583,
        "Sector1SessionTime": None,
        "Sector2SessionTime": 1064838,
        "Sector3SessionTime": 1098400,
        "SpeedI1": 205.0,
        "SpeedI2": 110.0,
        "SpeedFL": 284.0,
        "SpeedST": 266.0,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1.0,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 979230,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": None,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }


def test_get_laps_with_driver_numbers_only():
    response = client_with_auth.get("/laps/2023/5?driver_number=1&driver_number=44")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == {
        "Time": 3868310,
        "Driver": "VER",
        "DriverNumber": "1",
        "LapTime": 101724,
        "LapNumber": 1.0,
        "Stint": 1.0,
        "PitOutTime": None,
        "PitInTime": None,
        "Sector1Time": None,
        "Sector2Time": 36216,
        "Sector3Time": 26263,
        "Sector1SessionTime": None,
        "Sector2SessionTime": 3842065,
        "Sector3SessionTime": 3868409,
        "SpeedI1": 212.0,
        "SpeedI2": 186.0,
        "SpeedFL": 274.0,
        "SpeedST": 306.0,
        "IsPersonalBest": False,
        "Compound": "HARD",
        "TyreLife": 1.0,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 3766300,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": 9.0,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }


def test_get_laps_with_session_and_driver_numbers():
    response = client_with_auth.get("/laps/2023/5?session=4&driver_number=1&driver_number=44")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == {
        "Time": 1087970,
        "Driver": "VER",
        "DriverNumber": "1",
        "LapTime": None,
        "LapNumber": 1.0,
        "Stint": 1.0,
        "PitOutTime": 972293,
        "PitInTime": None,
        "Sector1Time": None,
        "Sector2Time": 44852,
        "Sector3Time": 31773,
        "Sector1SessionTime": None,
        "Sector2SessionTime": 1056197,
        "Sector3SessionTime": 1088025,
        "SpeedI1": 202.0,
        "SpeedI2": 79.0,
        "SpeedFL": 283.0,
        "SpeedST": 257.0,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1.0,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 972293,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": None,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }


# endregion good inputs

# region bad inputs


def test_get_laps_mixed_driver_numbers():
    response = client_with_auth.get(
        "/laps/2023/5?driver_number=0&driver_number=1&driver_number=13&driver_number=44&driver_number=83"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == {
        "Time": 3868310,
        "Driver": "VER",
        "DriverNumber": "1",
        "LapTime": 101724,
        "LapNumber": 1.0,
        "Stint": 1.0,
        "PitOutTime": None,
        "PitInTime": None,
        "Sector1Time": None,
        "Sector2Time": 36216,
        "Sector3Time": 26263,
        "Sector1SessionTime": None,
        "Sector2SessionTime": 3842065,
        "Sector3SessionTime": 3868409,
        "SpeedI1": 212.0,
        "SpeedI2": 186.0,
        "SpeedFL": 274.0,
        "SpeedST": 306.0,
        "IsPersonalBest": False,
        "Compound": "HARD",
        "TyreLife": 1.0,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 3766300,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": 9.0,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }


def test_get_laps_bad_driver_numbers():
    response = client_with_auth.get(
        "/laps/2023/5?driver_number=0&driver_number=99&driver_number=13&driver_number=45&driver_number=83"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_get_laps_bad_round():
    response = client_with_auth.get("/laps/2023/24")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Bad Request. Invalid round: 24"}


# endregion bad inputs
