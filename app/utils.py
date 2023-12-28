from app.constants import DEFAULT_TESTING_YEAR


def get_default_year() -> int:
    # TODO default year contains atleast one session data

    return DEFAULT_TESTING_YEAR


def range_inclusive(start: int, end: int) -> range:
    return range(start, end + 1)
