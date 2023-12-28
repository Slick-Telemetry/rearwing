import json
from typing import Annotated

import fastf1
from fastapi import FastAPI, Path

from app.constants import EVENT_SCHEDULE_DATETIME_DTYPE_LIST, METADATA_DESCRIPTION
from app.models import Schedule
from app.utils import get_default_year

app = FastAPI(
    title="Slick Telemetry API",
    description=METADATA_DESCRIPTION,
    version="0.1.0",
    contact={
        "name": "Slick Telemetry",
        "url": "https://github.com/Slick-Telemetry",
        "email": "",
    },
    license_info={
        "name": "GNU General Public License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
)


@app.get("/")
def read_root():
    return {"We Are": "SlickTelemetry"}


@app.get("/schedule/{year}", response_model=list[Schedule])
def get_schedule_for_year(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the schedule",
            gt=1949,  # Supported years are 1950 to current
            lt=get_default_year() + 1,
        ),
    ]
) -> list[Schedule]:
    event_schedule = fastf1.get_event_schedule(year)

    # Convert timestamp(z) related columns' data into a string type
    # https://stackoverflow.com/questions/50404559/python-error-typeerror-object-of-type-timestamp-is-not-json-serializable
    for col in EVENT_SCHEDULE_DATETIME_DTYPE_LIST:
        event_schedule[col] = event_schedule[col].astype(str)

    # Convert the dataframe to a JSON string
    event_schedule_as_json = event_schedule.to_json(orient="records")

    # Parse the JSON string to a JSON object
    event_schedule_as_json_obj = json.loads(event_schedule_as_json)

    return event_schedule_as_json_obj
