# Built-in
import json
import logging
from datetime import datetime
from typing import Annotated, List

# External
import fastf1
from fastapi import FastAPI, HTTPException, Path, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastf1.ergast import Ergast
from pandas import Timestamp

# App
from .constants import (
    DEFAULT_SESSION,
    EVENT_SCHEDULE_DATETIME_DTYPE_LIST,
    MAX_SUPPORTED_ROUND,
    MAX_SUPPORTED_SESSION,
    MAX_SUPPORTED_YEAR,
    METADATA_DESCRIPTION,
    MIN_SUPPORTED_ROUND,
    MIN_SUPPORTED_SESSION,
    MIN_SUPPORTED_YEAR,
)
from .models import EventSchedule, HealthCheck, Laps, Results, Schedule, Standings
from .utils import get_default_year


# fastf1.set_log_level("WARNING") # TODO use for production and staging

# Cors Middleware
origins = ["http://localhost:3000"]
# Ergast configuration
ergast = Ergast(result_type="raw", auto_cast=True)
# Others
favicon_path = "favicon.ico"

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


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
    summary="Get events schedule for a given year",
    response_description="Return list of events schedule for a given year",
    status_code=status.HTTP_200_OK,
    response_model=Schedule,
)
def get_schedule(
    year: Annotated[
        int | None,
        Query(
            title="The year for which to get the schedule",
            description="The year for which to get the schedule",
            ge=MIN_SUPPORTED_YEAR,
            le=MAX_SUPPORTED_YEAR,
        ),
    ] = None,
) -> Schedule:
    """
    ## Get events schedule for a given year
    Endpoint to get events schedule for a given year.

    **NOTE**: If `year` is not provided; we use the default year. Default year is defined as the year which has data for at least 1 race session.

    **Returns**:
        Schedule: Returns a JSON response with the list of event schedule
    """

    if year is None:
        year = get_default_year()

    event_schedule = fastf1.get_event_schedule(year, include_testing=False)

    # Convert timestamp(z) related columns' data into string type
    # https://stackoverflow.com/questions/50404559/python-error-typeerror-object-of-type-timestamp-is-not-json-serializable
    for col in EVENT_SCHEDULE_DATETIME_DTYPE_LIST:
        event_schedule[col] = event_schedule[col].astype(str)

    # Convert the dataframe to a JSON string
    event_schedule_as_json = event_schedule.to_json(orient="records")

    # Parse the JSON string to a JSON object
    event_schedule_as_json_obj: List[EventSchedule] = json.loads(event_schedule_as_json)
    schedule_as_json_obj: Schedule = Schedule.model_validate(
        {
            "year": year,
            "EventSchedule": event_schedule_as_json_obj,
        }
    )

    return schedule_as_json_obj


@app.get(
    "/next-event",
    tags=["schedule"],
    summary="Get upcoming event",
    response_description="Returns upcoming event",
    status_code=status.HTTP_200_OK,
    response_model=EventSchedule,
)
def get_next_event() -> EventSchedule:
    """
    ## Get upcoming event
    Endpoint to get upcoming event.

    **Returns**:
        EventSchedule: Returns upcoming event
    """

    remaining_events = fastf1.get_events_remaining(dt=datetime.now(), include_testing=False)

    if len(remaining_events) == 0:
        # EITHER current season has ended OR new season's schedule has not yet been released

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Next event not found.")
    else:
        # Current season EITHER has not yet started OR is in progress

        next_event: fastf1.events.Event = remaining_events.iloc[0]

        # Convert timestamp(z) related columns' data into string type
        next_event = next_event.apply(
            lambda x: str(x) if isinstance(x, Timestamp) else x,
        )

        # Convert the series to a JSON string
        next_event_as_json = next_event.to_json()

        # Parse the JSON string to a JSON object
        next_event_as_json_obj: EventSchedule = json.loads(next_event_as_json)

        return next_event_as_json_obj


@app.get(
    "/standings",
    tags=["standings"],
    summary="Get drivers and constructors standing for a given year and round",
    response_description="Return a list of drivers and constructors standings at specific points of a season for a given year and round. If the season hasn't ended you get the current standings.",
    status_code=status.HTTP_200_OK,
    response_model=Standings,
)
def get_standings(
    year: Annotated[
        int | None,
        Query(
            title="The year for which to get the driver and constructors standing. If the season hasn't ended you get the current standings.",
            description="The year for which to get the driver and constructors standing. If the season hasn't ended you get the current standings.",
            ge=MIN_SUPPORTED_YEAR,
            le=MAX_SUPPORTED_YEAR,
        ),
    ] = None,
    round: Annotated[
        int | None,
        Query(
            title="The round in a year for which to get the driver and constructor standings",
            description="The round in a year for which to get the driver and constructor standings",
            ge=MIN_SUPPORTED_ROUND,
            le=MAX_SUPPORTED_ROUND,
        ),
    ] = None,
) -> Standings:
    """
    ## Get driver and constructor standings for a given year and round
    Endpoint to get driver and constructor standings at specific points of a season for a given year and round. If the season hasn't ended you get the current standings.

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
        data: Standings = Standings.model_validate(
            {
                "season": driver_standings[0]["season"],
                "round": driver_standings[0]["round"],
                "DriverStandings": driver_standings[0]["DriverStandings"],
                "ConstructorStandings": constructor_standings[0]["ConstructorStandings"],
            }
        )
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver standings not found.")
    else:
        # something went wrong, investigate
        raise HTTPException(status_code=500, detail="Something went wrong. Investigate!")


@app.get(
    "/results/{year}/{round}",
    tags=["results"],
    summary="Get session results for a given year, round and session",
    response_description="Return session results for a given year, round and session.",
    status_code=status.HTTP_200_OK,
    response_model=List[Results],
)
def get_results(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the results",
            description="The year for which to get the results",
            ge=MIN_SUPPORTED_YEAR,
            le=MAX_SUPPORTED_YEAR,
        ),
    ],
    round: Annotated[
        int,
        Path(
            title="The round in a year for which to get the results",
            description="The round in a year for which to get the results",
            ge=MIN_SUPPORTED_ROUND,
            le=MAX_SUPPORTED_ROUND,
        ),
    ],
    session: Annotated[
        int,
        Query(
            title="The session in a round for which to get the results",
            description="The session in a round for which to get the results. (Default = 5; ie race)",
            ge=MIN_SUPPORTED_SESSION,
            le=MAX_SUPPORTED_SESSION,
        ),
    ] = DEFAULT_SESSION,
) -> List[Results]:
    """
    ## Get session results for a given year, round and session
    Endpoint to get session results for a given year, round and session.

    **NOTE**: If `session` is not provided; we use the default session. Default = 5; ie race.

    **Returns**:
        List[Results]: Returns a JSON response with the list of session results
    """

    try:
        session_obj = fastf1.get_session(year=year, gp=round, identifier=session)
        session_obj.load(
            laps=False,
            telemetry=False,
            weather=False,
            messages=False,
        )
        session_results = session_obj.results

        # Convert the dataframe to a JSON string
        session_results_as_json = session_results.to_json(orient="records")

        # Parse the JSON string to a JSON object
        session_results_as_json_obj: List[Results] = json.loads(session_results_as_json)
        return session_results_as_json_obj

    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request. {str(ve)}")
    except KeyError as ke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Likely an error when fetching results data for a session that has yet to happen. {str(ke)}",
        )


@app.get(
    "/laps/{year}/{round}",
    tags=["laps"],
    summary="Get laps of one or more drivers for a given year, round and session",
    response_description="Return laps of one or more drivers for a given year, round and session.",
    status_code=status.HTTP_200_OK,
    response_model=List[Laps],
)
def get_laps(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the laps",
            description="The year for which to get the laps",
            ge=MIN_SUPPORTED_YEAR,
            le=MAX_SUPPORTED_YEAR,
        ),
    ],
    round: Annotated[
        int,
        Path(
            title="The round in a year for which to get the laps",
            description="The round in a year for which to get the laps",
            ge=MIN_SUPPORTED_ROUND,
            le=MAX_SUPPORTED_ROUND,
        ),
    ],
    session: Annotated[
        int,
        Query(
            title="The session in a round for which to get the laps",
            description="The session in a round for which to get the laps. (Default = 5; ie race)",
            ge=MIN_SUPPORTED_SESSION,
            le=MAX_SUPPORTED_SESSION,
        ),
    ] = DEFAULT_SESSION,
    driver_numbers: Annotated[
        List[int],
        Query(
            title="List of drivers for whom to get the laps",
            description="List of drivers for whom to get the laps",
        ),
    ] = [],
) -> List[Laps]:
    """
    ## Get laps of one or more drivers for a given year, round and session
    Endpoint to get laps of one or more drivers for a given year, round and session.

    **NOTE**:
    - If `session` is not provided; we use the default session. Default = 5; ie race.
    - If no `driver_numbers` are provided; you get laps for all drivers.

    **Returns**:
        List[Laps]: Returns a JSON response with the list of session results
    """

    session_obj = fastf1.get_session(year=year, gp=round, identifier=session)
    session_obj.load(
        laps=True,
        telemetry=False,
        weather=False,
        messages=True,  # required for `Deleted` and `DeletedReason`
    )
    session_laps = session_obj.laps

    try:
        if len(driver_numbers) > 0:
            session_laps = session_laps.pick_drivers(driver_numbers)

        # Convert the dataframe to a JSON string
        session_laps_as_json = session_laps.to_json(orient="records")

        # Parse the JSON string to a JSON object
        session_laps_as_json_obj: List[Laps] = json.loads(session_laps_as_json)

        return session_laps_as_json_obj
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request. {str(ve)}")
    except KeyError as ke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Likely an error when fetching laps data for a session that has yet to happen. {str(ke)}",
        )
