import json
from typing import Annotated, Literal

import fastf1
from fastapi import FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastf1.ergast import Ergast

from app.constants import (
    EVENT_SCHEDULE_DATETIME_DTYPE_LIST,
    MAX_SUPPORTED_ROUND_FOR_STANDINGS,
    MAX_SUPPORTED_YEAR_FOR_SCHEDULE,
    METADATA_DESCRIPTION,
    MIN_SUPPORTED_ROUND_FOR_STANDINGS,
    MIN_SUPPORTED_YEAR_FOR_SCHEDULE,
)
from app.models import HealthCheck, Schedule, Standings
from app.utils import get_default_year_for_schedule

# fastf1.set_log_level("WARNING") # TODO use for production and staging

# Cors Middleware
origins = ["http://localhost:3000"]
# Ergast configuration
ergast = Ergast(result_type="raw", auto_cast=True)


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


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # HTTPSRedirectMiddleware # TODO use for production and staging
)


@app.get(
    "/",
    tags=["root"],
    summary="Read root",
    response_description="Return root info",
    status_code=status.HTTP_200_OK,
)
def read_root():
    return {"we_are": "SlickTelemetry"}


# https://gist.github.com/Jarmos-san/0b655a3f75b698833188922b714562e5
@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).

    **Returns**:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")


@app.get(
    "/schedule",
    tags=["schedule"],
    summary="Get events schedule for a Formula 1 calendar year",
    response_description="Return list of events schedule for a Formula 1 calendar year",
    status_code=status.HTTP_200_OK,
    response_model=list[Schedule],
)
def get_schedule(
    year: Annotated[
        int | None,
        Query(
            title="The year for which to get the schedule",
            ge=MIN_SUPPORTED_YEAR_FOR_SCHEDULE,
            le=MAX_SUPPORTED_YEAR_FOR_SCHEDULE,
        ),
    ] = None
) -> list[Schedule]:
    """
    ## Get events schedule for a Formula 1 calendar year
    Endpoint to get events schedule for Formula 1 calendar year.

    **Returns**:
        list[Schedule]: Returns a JSON response with the list of event schedule
    """
    if year is None:
        year = get_default_year_for_schedule()

    event_schedule = fastf1.get_event_schedule(year)

    # Convert timestamp(z) related columns' data into string type
    # https://stackoverflow.com/questions/50404559/python-error-typeerror-object-of-type-timestamp-is-not-json-serializable
    for col in EVENT_SCHEDULE_DATETIME_DTYPE_LIST:
        event_schedule[col] = event_schedule[col].astype(str)

    # Convert the dataframe to a JSON string
    event_schedule_as_json = event_schedule.to_json(orient="records")

    # Parse the JSON string to a JSON object
    event_schedule_as_json_obj = json.loads(event_schedule_as_json)

    return event_schedule_as_json_obj


@app.get(
    "/standings",
    tags=["standings"],
    summary="Get drivers and contructors standings ",
    response_description="Return a list of drivers and contructors standings at specific points of a season. If the season hasn't ended you will get the current standings.",
    status_code=status.HTTP_200_OK,
    response_model=Standings,
)
def get_standings(
    year: Annotated[
        int | None,
        Query(
            title="The year for which to get the driver and contructors standing. If the season hasn't ended you will get the current standings.",
            ge=MIN_SUPPORTED_YEAR_FOR_SCHEDULE,
            le=MAX_SUPPORTED_YEAR_FOR_SCHEDULE,
        ),
    ] = None,
    round: Annotated[
        Literal["last"] | int | None,
        Query(
            title="The round in a year for which to get the driver and contructor standings",
            ge=MIN_SUPPORTED_ROUND_FOR_STANDINGS,
            le=MAX_SUPPORTED_ROUND_FOR_STANDINGS,
        ),
    ] = None,
) -> Standings:
    """
    ## Get driver and contructor standings
    Endpoint to get driver and contructor standings at specific points of a season. If the season hasn't ended you will get the current standings.

    **Returns**:
        Standings: Returns a JSON response with the driver and constructor standings
    """

    if year is None and round is None:
        # neither year nor round are provided; get results for the last round of the default year
        year = get_default_year_for_schedule()
        round = "last"
    elif year is None and round is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bad request. Must provide the "year" parameter.',
        )
    elif year is not None and round is None:
        # only year is provided; get results for last round of that year
        round = "last"

    driver_standings = ergast.get_driver_standings(season=year, round=round)
    constructor_standings = ergast.get_constructor_standings(season=year, round=round)
    data: Standings = {}

    if len(driver_standings) > 0 and len(constructor_standings) > 0:
        data = {
            "season": driver_standings[0]["season"],
            "round": driver_standings[0]["round"],
            "DriverStandings": driver_standings[0]["DriverStandings"],
            "ConstructorStandings": constructor_standings[0]["ConstructorStandings"],
        }

    return data
