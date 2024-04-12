# App
from . import client_with_auth


def test_get_next_event(snapshot):
    response = client_with_auth.get("/next-event")
    snapshot.assert_match(response.json())
