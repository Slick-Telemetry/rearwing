# App
from . import client_with_auth


# region good inputs


def test_get_standings(snapshot):
    response = client_with_auth.get("/standings")
    snapshot.assert_match(response.json())


def test_get_standings_good_year_only(snapshot):
    response = client_with_auth.get("/standings?year=2023")
    snapshot.assert_match(response.json())


def test_get_standings_good_year_and_round(snapshot):
    response = client_with_auth.get("/standings?year=2023&round=5")
    snapshot.assert_match(response.json())


# endregion good inputs

# region no inputs


def test_get_standings_bad_year_no_input(snapshot):
    response = client_with_auth.get("/standings?round=3")
    snapshot.assert_match(response.json())


# endregion no inputs
