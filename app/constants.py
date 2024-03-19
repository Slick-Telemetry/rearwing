# Built-in
from datetime import datetime


EVENT_SCHEDULE_DATETIME_DTYPE_LIST = [
    "EventDate",
    "Session1Date",
    "Session1DateUtc",
    "Session2Date",
    "Session2DateUtc",
    "Session3Date",
    "Session3DateUtc",
    "Session4Date",
    "Session4DateUtc",
    "Session5Date",
    "Session5DateUtc",
]

MIN_YEAR_SUPPORTED = 1950
MIN_YEAR_WITH_TELEMETRY_SUPPORTED = 2018
MAX_YEAR_SUPPORTED = datetime.today().year

MIN_ROUND_SUPPORTED = 1  # testing events all share round number = 0
MAX_ROUND_SUPPORTED = 25

MIN_SESSION_SUPPORTED = 1
MAX_SESSION_SUPPORTED = 5

DEFAULT_SESSION = 5  # race

MIN_DRIVER_NUMBER_SUPPORTED = 1
MAX_DRIVER_NUMBER_SUPPORTED = 99

MIN_LAP_COUNT_SUPPORTED = 1
MAX_LAP_COUNT_SUPPORTED = 80
