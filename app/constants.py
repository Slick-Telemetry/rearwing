# Built-in
from datetime import datetime


METADATA_DESCRIPTION = """
Slick Telemetry backend written in python with fastf1. 🏎 
"""

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

MIN_SUPPORTED_YEAR = 1950
MAX_SUPPORTED_YEAR = datetime.today().year

MIN_SUPPORTED_ROUND = 1  # testing events all share round number = 0
MAX_SUPPORTED_ROUND = 25

MIN_SUPPORTED_SESSION = 1
MAX_SUPPORTED_SESSION = 5

DEFAULT_SESSION = 5  # race

MIN_SUPPORTED_DRIVER_NUMBER = 1
MAX_SUPPORTED_DRIVER_NUMBER = 99

MIN_SUPPORTED_LAP_COUNT = 1
