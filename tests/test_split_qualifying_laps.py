# External
from fastapi import status

# App
from . import client_with_auth


# region good inputs


def test_get_split_qualifying_laps():
    response = client_with_auth.get("/split-qualifying-laps/2023/6")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["Q1"][0] == {
        "Time": 952796,
        "Driver": "VER",
        "DriverNumber": "1",
        "LapTime": 109496,
        "LapNumber": 1,
        "Stint": 1,
        "PitOutTime": 845753,
        "PitInTime": None,
        "Sector1Time": 40759,
        "Sector2Time": 43892,
        "Sector3Time": 24845,
        "Sector1SessionTime": 884112,
        "Sector2SessionTime": 927987,
        "Sector3SessionTime": 952830,
        "SpeedI1": 121,
        "SpeedI2": 178,
        "SpeedFL": 270,
        "SpeedST": 270,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 845753,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": None,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }
    assert response.json()["Q2"][0] == {
        "Time": 3020807,
        "Driver": "VER",
        "DriverNumber": "1",
        "LapTime": None,
        "LapNumber": 13,
        "Stint": 3,
        "PitOutTime": 2935323,
        "PitInTime": None,
        "Sector1Time": None,
        "Sector2Time": 39705,
        "Sector3Time": 20790,
        "Sector1SessionTime": None,
        "Sector2SessionTime": 3000041,
        "Sector3SessionTime": 3020978,
        "SpeedI1": 184,
        "SpeedI2": 174,
        "SpeedFL": 265,
        "SpeedST": 261,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 2935323,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": None,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }
    assert response.json()["Q3"][0] == {
        "Time": 4399675,
        "Driver": "VER",
        "DriverNumber": "1",
        "LapTime": None,
        "LapNumber": 22,
        "Stint": 5,
        "PitOutTime": 4314995,
        "PitInTime": None,
        "Sector1Time": None,
        "Sector2Time": 38757,
        "Sector3Time": 20605,
        "Sector1SessionTime": None,
        "Sector2SessionTime": 4379088,
        "Sector3SessionTime": 4399869,
        "SpeedI1": 182,
        "SpeedI2": 184,
        "SpeedFL": 265,
        "SpeedST": 263,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1,
        "FreshTyre": True,
        "Team": "Red Bull Racing",
        "LapStartTime": 4314995,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": None,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }


def test_get_split_qualifying_laps_with_driver_numbers():
    response = client_with_auth.get("/split-qualifying-laps/2023/6?driver_number=14&driver_number=44")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["Q1"][0] == {
        "Time": 1009351,
        "Driver": "ALO",
        "DriverNumber": "14",
        "LapTime": 89950,
        "LapNumber": 1,
        "Stint": 1,
        "PitOutTime": 920127,
        "PitInTime": None,
        "Sector1Time": 24847,
        "Sector2Time": 42205,
        "Sector3Time": 22898,
        "Sector1SessionTime": 944283,
        "Sector2SessionTime": 986486,
        "Sector3SessionTime": 1009517,
        "SpeedI1": 182,
        "SpeedI2": 173,
        "SpeedFL": 268,
        "SpeedST": 261,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1,
        "FreshTyre": True,
        "Team": "Aston Martin",
        "LapStartTime": 920127,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": None,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }
    assert response.json()["Q2"][0] == {
        "Time": 3068521,
        "Driver": "ALO",
        "DriverNumber": "14",
        "LapTime": 96499,
        "LapNumber": 11,
        "Stint": 3,
        "PitOutTime": 2973745,
        "PitInTime": None,
        "Sector1Time": 29931,
        "Sector2Time": 41348,
        "Sector3Time": 25220,
        "Sector1SessionTime": 3001953,
        "Sector2SessionTime": 3043301,
        "Sector3SessionTime": 3068521,
        "SpeedI1": 178,
        "SpeedI2": 181,
        "SpeedFL": 268,
        "SpeedST": 252,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1,
        "FreshTyre": True,
        "Team": "Aston Martin",
        "LapStartTime": 2972022,
        "LapStartDate": None,
        "TrackStatus": "1",
        "Position": None,
        "Deleted": False,
        "DeletedReason": "",
        "FastF1Generated": False,
        "IsAccurate": False,
    }
    assert response.json()["Q3"][0] == {
        "Time": 4425334,
        "Driver": "ALO",
        "DriverNumber": "14",
        "LapTime": 96409,
        "LapNumber": 20,
        "Stint": 5,
        "PitOutTime": 4331729,
        "PitInTime": None,
        "Sector1Time": 34209,
        "Sector2Time": 40051,
        "Sector3Time": 22149,
        "Sector1SessionTime": 4363134,
        "Sector2SessionTime": 4403185,
        "Sector3SessionTime": 4425334,
        "SpeedI1": 185,
        "SpeedI2": 183,
        "SpeedFL": 267,
        "SpeedST": 260,
        "IsPersonalBest": False,
        "Compound": "SOFT",
        "TyreLife": 1,
        "FreshTyre": True,
        "Team": "Aston Martin",
        "LapStartTime": 4328925,
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


def test_get_split_qualifying_laps_bad_driver_numbers():
    response = client_with_auth.get("/split-qualifying-laps/2023/6?driver_number=45&driver_number=83")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Q1": None, "Q2": None, "Q3": None}


def test_get_split_qualifying_laps_bad_round():
    response = client_with_auth.get("/split-qualifying-laps/2023/24")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Bad Request. Invalid round: 24"}


# endregion bad inputs
