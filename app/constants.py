from datetime import datetime

METADATA_DESCRIPTION = """
Slick Telemetry backend written in python with fastf1. 🏎 
    
## Schedule

You can query Formula 1 schedule by **year**.
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

MIN_SUPPORTED_ROUND = 1
MAX_SUPPORTED_ROUND = 30
