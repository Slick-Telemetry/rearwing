# Built-in
import logging
from datetime import datetime

# External
import fastf1


logger = logging.getLogger(__name__)

BACKSTOP = 1954


def get_default_year() -> int:
    """Get the default year for the app.

    NOTE - The default year is defined as the latest year which has data for at least 1 race session.
    """

    default_year = datetime.today().year

    while default_year >= BACKSTOP:
        event_schedule = fastf1.get_event_schedule(default_year, include_testing=False)
        if len(event_schedule) == 0:
            # if no data is found, check previous year
            default_year -= 1
            continue
        try:
            # extract first race's round number.
            # per current (2023-01-22) fastf1/ergast implementation, the value is 1.
            race_event_round_number = event_schedule.iloc[0]["RoundNumber"]
            # create a fastf1.core.Session object
            first_race_event_session_obj = fastf1.get_session(default_year, race_event_round_number, "Race")
            # load session data
            first_race_event_session_obj.load()
        except (ValueError, KeyError) as ex:
            # capture errors occurred during extracting first race's round number and loading the session data
            logger.exception(ex)
            default_year -= 1
        else:
            return default_year
    raise ValueError(f"No data found for years upto {BACKSTOP}")
