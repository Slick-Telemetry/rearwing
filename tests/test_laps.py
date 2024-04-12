# App
from . import client_with_auth


# region good inputs


def test_get_laps(snapshot):
    response = client_with_auth.get("/laps/2023/5")
    snapshot.assert_match(response.json())


def test_get_laps_with_session_only(snapshot):
    response = client_with_auth.get("/laps/2023/5?session=4")
    snapshot.assert_match(response.json())


def test_get_laps_with_driver_numbers_only(snapshot):
    response = client_with_auth.get("/laps/2023/5?driver_number=1&driver_number=44")
    snapshot.assert_match(response.json())


def test_get_laps_with_session_and_driver_numbers(snapshot):
    response = client_with_auth.get("/laps/2023/5?session=4&driver_number=1&driver_number=44")
    snapshot.assert_match(response.json())


# endregion good inputs

# region bad inputs


def test_get_laps_mixed_driver_numbers(snapshot):
    response = client_with_auth.get(
        "/laps/2023/5?driver_number=0&driver_number=1&driver_number=13&driver_number=44&driver_number=83"
    )
    snapshot.assert_match(response.json())


def test_get_laps_bad_driver_numbers(snapshot):
    response = client_with_auth.get(
        "/laps/2023/5?driver_number=0&driver_number=99&driver_number=13&driver_number=45&driver_number=83"
    )
    snapshot.assert_match(response.json())


def test_get_laps_bad_round(snapshot):
    response = client_with_auth.get("/laps/2023/24")
    snapshot.assert_match(response.json())


# endregion bad inputs
