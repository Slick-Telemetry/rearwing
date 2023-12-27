import json

import fastf1
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from constants import EVENT_SCHEDULE_DATETIME_DTYPE_LIST
from utils import get_default_year

app = FastAPI()


@app.get("/")
def read_root():
    return {"We Are": "SlickTelemetry"}


@app.get("/schedule/{year}")
def schedule(year: int = get_default_year()):
    event_schedule = fastf1.get_event_schedule(year)

    # Convert timestamp(z) related columns' data into a string type
    # https://stackoverflow.com/questions/50404559/python-error-typeerror-object-of-type-timestamp-is-not-json-serializable
    for col in EVENT_SCHEDULE_DATETIME_DTYPE_LIST:
        event_schedule[col] = event_schedule[col].astype(str)

    # Convert the dataframe to a JSON string
    event_schedule_as_json = event_schedule.to_json(orient="records")

    # Parse the JSON string to a JSON object
    event_schedule_as_json_obj = json.loads(event_schedule_as_json)

    return JSONResponse(content=event_schedule_as_json_obj)
