# App
from . import client_with_auth


# region good inputs


def test_get_split_qualifying_laps(snapshot):
    response = client_with_auth.get("/split-qualifying-laps/2023/6")
    snapshot.assert_match(response.json())


def test_get_split_qualifying_laps_with_driver_numbers(snapshot):
    response = client_with_auth.get("/split-qualifying-laps/2023/6?driver_number=14&driver_number=44")
    snapshot.assert_match(response.json())


# endregion good inputs

# region bad inputs


def test_get_split_qualifying_laps_bad_driver_numbers(snapshot):
    response = client_with_auth.get("/split-qualifying-laps/2023/6?driver_number=45&driver_number=83")
    snapshot.assert_match(response.json())


def test_get_split_qualifying_laps_bad_round(snapshot):
    response = client_with_auth.get("/split-qualifying-laps/2023/24")
    snapshot.assert_match(response.json())


# endregion bad inputs
