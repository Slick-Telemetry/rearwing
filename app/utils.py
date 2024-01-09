from datetime import datetime

import fastf1


def get_default_year_for_schedule() -> int:
    # default year is defined as the year which has data for atleast 1 race session

    current_year = datetime.today().year
    event_schedule = fastf1.get_event_schedule(current_year, include_testing=False)

    if len(event_schedule) == 0:
        return current_year - 1

    try:
        first_event_round_number = event_schedule.iloc[0]["RoundNumber"]
        first_event_session = fastf1.get_session(
            current_year, first_event_round_number, "Race"
        )
        first_event_session.load()
    except (ValueError, KeyError):
        return current_year - 1

    return current_year - 1
