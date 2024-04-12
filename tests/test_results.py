# App
from . import client_with_auth


# region good inputs


def test_get_results(snapshot):
    response = client_with_auth.get("/results/2023/5")
    snapshot.assert_match(response.json())


def test_get_results_with_session(snapshot):
    response = client_with_auth.get("/results/2023/5?session=4")
    snapshot.assert_match(response.json())


# endregion good inputs

# region bad inputs


def test_get_results_bad_round_invalid(snapshot):
    response = client_with_auth.get("/results/2023/25?session=2")
    snapshot.assert_match(response.json())


# endregion bad inputs
