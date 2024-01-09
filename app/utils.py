import datetime

import fastf1


def get_default_year_for_schedule() -> int:
    # TODO default year is defined as the year which has data for atleast 1 session
    # get current year
    # get first race event from that year
    # get relevant race session from that event
    # get race data
    # if available default is current year, else last year

    current_year = datetime.datetime.now().current_year
    default_year = current_year
    event_schedule = fastf1.get_event_schedule(default_year, include_testing=False)

    if len(event_schedule) == 0:
        return default_year - 1

    try:
        first_event_round_number = event_schedule.iloc[0]["RoundNumber"]
        first_event_session = fastf1.get_session(
            default_year, first_event_round_number, "Race"
        )
        first_event_session.load()
    except ValueError:
        return default_year - 1

    return default_year - 1
