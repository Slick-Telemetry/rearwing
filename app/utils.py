# Built-in
from datetime import datetime

# External
import fastf1


def get_default_year() -> int:
    # default year is defined as the year which has data for at least 1 race session

    current_year = datetime.today().year
    event_schedule = fastf1.get_event_schedule(current_year, include_testing=False)

    if len(event_schedule) == 0:
        # if no data is found, return previous year
        return current_year - 1

    try:
        # extract first race's round number.
        # per current (2023-01-22) fastf1/ergast implementation, the value is 1.
        race_event_round_number = event_schedule.iloc[0]["RoundNumber"]
        # create a fastf1.core.Session object
        first_race_event_session_obj = fastf1.get_session(current_year, race_event_round_number, "Race")
        # load session data
        first_race_event_session_obj.load()
    except (ValueError, KeyError):
        # capture errors occurred during extracting first race's round number and loading the session data
        return current_year - 1

    return current_year
