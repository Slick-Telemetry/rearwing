import json
from typing import Annotated, Literal

import fastf1
from fastapi import FastAPI, HTTPException, Path, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastf1.ergast import Ergast

from app.constants import (
    EVENT_SCHEDULE_DATETIME_DTYPE_LIST,
    MAX_SUPPORTED_ROUND,
    MAX_SUPPORTED_SESSION,
    MAX_SUPPORTED_YEAR,
    METADATA_DESCRIPTION,
    MIN_SUPPORTED_ROUND,
    MIN_SUPPORTED_SESSION,
    MIN_SUPPORTED_YEAR,
)
from app.models import HealthCheck, Results, Schedule, Standings
from app.utils import get_default_year

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
            ge=MIN_SUPPORTED_YEAR,
            le=MAX_SUPPORTED_YEAR,
        ),
    ] = None
) -> list[Schedule]:
    """
    ## Get events schedule for a Formula 1 calendar year
    Endpoint to get events schedule for Formula 1 calendar year.

    **NOTE**: If `year` is not provided; we use the default year. Default year is defined as the year which has data for at least 1 race session.

    **Returns**:
        list[Schedule]: Returns a JSON response with the list of event schedule
    """

    if year is None:
        year = get_default_year()

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
    summary="Get drivers and constructors standings ",
    response_description="Return a list of drivers and constructors standings at specific points of a season. If the season hasn't ended you will get the current standings.",
    status_code=status.HTTP_200_OK,
    response_model=Standings,
)
def get_standings(
    year: Annotated[
        int | None,
        Query(
            title="The year for which to get the driver and constructors standing. If the season hasn't ended you will get the current standings.",
            ge=MIN_SUPPORTED_YEAR,
            le=MAX_SUPPORTED_YEAR,
        ),
    ] = None,
    round: Annotated[
        int | None,
        Query(
            title="The round in a year for which to get the driver and constructor standings",
            ge=MIN_SUPPORTED_ROUND,
            le=MAX_SUPPORTED_ROUND,
        ),
    ] = None,
) -> Standings:
    """
    ## Get driver and constructor standings
    Endpoint to get driver and constructor standings at specific points of a season. If the season hasn't ended you will get the current standings.

    **NOTE**: If `year` is not provided; we use the default year. Default year is defined as the year which has data for at least 1 race session.

    **Returns**:
        Standings: Returns a JSON response with the driver and constructor standings
    """

    if year is None and round is None:
        # neither year nor round are provided; get results for the last round of the default year
        year = get_default_year()
    elif year is None and round is not None:
        # only round is provided; error out
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bad request. Must provide the "year" parameter.',
        )

    # inputs are good; either one of the two remaining cases:
    # 1. both year and round are provided
    # 2. only year is provided

    driver_standings = ergast.get_driver_standings(season=year, round=round)
    constructor_standings = ergast.get_constructor_standings(season=year, round=round)

    driver_standings_available = True if len(driver_standings) > 0 else False
    constructor_standings_available = True if len(constructor_standings) > 0 else False

    if driver_standings_available and constructor_standings_available:
        # both driver and constructor standings are available
        data: Standings = {
            "season": driver_standings[0]["season"],
            "round": driver_standings[0]["round"],
            "DriverStandings": driver_standings[0]["DriverStandings"],
            "ConstructorStandings": constructor_standings[0]["ConstructorStandings"],
        }
        return data
    elif not driver_standings_available and not constructor_standings_available:
        # neither driver nor constructor standings are available
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Driver and constructor standings not found.",
        )
    elif driver_standings_available:
        # only driver standings are available
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Constructor standings not found.",
        )
    elif constructor_standings_available:
        # only constructor standings are available
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Driver standings not found."
        )
    else:
        # something went wrong, investigate
        raise HTTPException(
            status_code=500, detail="Something went wrong. Investigate!"
        )


@app.get(
    "/results/{year}/{round}/{session}",
    tags=["results"],
    summary="Get session results for a given year, round and session",
    response_description="Return session results for a given year, round and session.",
    status_code=status.HTTP_200_OK,
    response_model=list[Results],
)
def get_results(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the results",
            ge=MIN_SUPPORTED_YEAR,
            le=MAX_SUPPORTED_YEAR,
        ),
    ],
    round: Annotated[
        int,
        Path(
            title="The round in a year for which to get the results",
            ge=MIN_SUPPORTED_ROUND,
            le=MAX_SUPPORTED_ROUND,
        ),
    ],
    session: Annotated[
        int,
        Path(
            title="The session in a round for which to get the results",
            ge=MIN_SUPPORTED_SESSION,
            le=MAX_SUPPORTED_SESSION,
        ),
    ],
) -> list[Results]:
    """
    ## Get session results for a given year, round and session
    Endpoint to get session results for a given year, round and session.

    **Returns**:
        list[Results]: Returns a JSON response with the list of session results
    """

    try:
        session_obj = fastf1.get_session(year=year, gp=round, identifier=session)
        session_obj.load(
            laps=True,
            telemetry=False,
            weather=False,
            messages=False,
        )
        session_results = session_obj.results

        # Convert the dataframe to a JSON string
        session_results_as_json = session_results.to_json(orient="records")

        # Parse the JSON string to a JSON object
        session_results_as_json_obj = json.loads(session_results_as_json)
        return session_results_as_json_obj

    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request. {str(ve)}"
        )
    except KeyError as ke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f". {str(ke)}"
        )
