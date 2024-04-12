# App
from . import client_with_auth


def test_get_schedule(snapshot):
    response = client_with_auth.get("/schedule")
    snapshot.assert_match(response.json())


def test_get_schedule_good_year(snapshot):
    response = client_with_auth.get("/schedule?year=2023")
    snapshot.assert_match(response.json())
