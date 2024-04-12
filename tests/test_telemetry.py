# App
from . import client_with_auth


# region good inputs


def test_get_telemetry(snapshot):
    response = client_with_auth.get("/telemetry/2023/4/1/1?session=5&weather=false")
    snapshot.assert_match(response.json())


def test_get_telemetry_with_weather(snapshot):
    response = client_with_auth.get("/telemetry/2023/4/1/1?session=5&weather=true")
    snapshot.assert_match(response.json())


# endregion good inputs

# region bad inputs


def test_get_telemetry_bad_round_invalid(snapshot):
    response = client_with_auth.get("/telemetry/2023/25/1/1?session=5&weather=false")
    snapshot.assert_match(response.json())


def test_get_telemetry_bad_driver_number(snapshot):
    response = client_with_auth.get("/telemetry/2023/4/3/1?session=5&weather=false")
    snapshot.assert_match(response.json())


def test_get_telemetry_bad_lap_not_found(snapshot):
    response = client_with_auth.get("/telemetry/2023/4/1/80?session=5&weather=false")
    snapshot.assert_match(response.json())


# endregion bad inputs
