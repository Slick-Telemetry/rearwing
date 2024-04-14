import newrelic.agent  # isort:skip

# Built-in
import os


if os.getenv("ENVIRONMENT") != "TEST":
    newrelic.agent.initialize("newrelic.ini")

# Built-in
import json
from datetime import datetime
from typing import Annotated, List

# External
import fastf1
from dotenv import dotenv_values
from fastapi import Depends, FastAPI, HTTPException, Path, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastf1.ergast import Ergast
from pandas import Timestamp

# App
from . import __version__
from .constants import (
    DEFAULT_SESSION,
    EVENT_SCHEDULE_DATETIME_DTYPE_LIST,
    MAX_DRIVER_NUMBER_SUPPORTED,
    MAX_LAP_COUNT_SUPPORTED,
    MAX_ROUND_SUPPORTED,
    MAX_SESSION_SUPPORTED,
    MAX_YEAR_SUPPORTED,
    MIN_DRIVER_NUMBER_SUPPORTED,
    MIN_LAP_COUNT_SUPPORTED,
    MIN_ROUND_SUPPORTED,
    MIN_SESSION_SUPPORTED,
    MIN_YEAR_SUPPORTED,
)
from .models import (
    EventSchedule,
    ExtendedTelemetry,
    HealthCheck,
    Laps,
    Results,
    Root,
    Schedule,
    SplitQualifyingLaps,
    Standings,
    Telemetry,
    Weather,
)
from .utils import get_default_year


# Load environment variables from .env file
config = dotenv_values(".env")
# FastF1 configuration
fastf1.set_log_level("WARNING")
fastf1.Cache.set_disabled()
# Ergast configuration
ergast = Ergast(result_type="raw", auto_cast=True)
# Cors Middleware
origins = [config["FRONTEND_URL"]]
# Others
favicon_path = "favicon.ico"
# Security
security = HTTPBearer()

app = FastAPI(
    title="Slick Telemetry API",
    description="Slick Telemetry backend written in python with fastf1. 🏎",
    version=__version__,
    contact={
        "name": "Slick Telemetry",
        "url": "https://github.com/Slick-Telemetry",
        "email": "",
    },
    license_info={
        "name": "GNU General Public License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    redoc_url=None,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # HTTPSRedirectMiddleware # TODO use for production and staging
)


def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Validates the token provided in the HTTP Authorization header.

    Parameters:
    - credentials: The HTTPAuthorizationCredentials object containing the token.

    Raises:
    - HTTPException: If the token is invalid.
    """
    if credentials.credentials != config["SECRET_TOKEN"]:
        raise HTTPException(status_code=403, detail="Invalid token")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@newrelic.agent.web_transaction()
@app.get(
    "/",
    tags=["root"],
    summary="Read root",
    response_description="Return root info",
    status_code=status.HTTP_200_OK,
    response_model=Root,
)
def read_root():
    return {"we_are": "SlickTelemetry"}


@newrelic.agent.web_transaction()
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


@newrelic.agent.web_transaction()
@app.get(
    "/schedule",
    tags=["schedule"],
    summary="Get events schedule for a given year",
    response_description="Return list of events schedule for a given year",
    status_code=status.HTTP_200_OK,
    response_model=Schedule,
    dependencies=[Depends(validate_token)],
)
def get_schedule(
    year: Annotated[
        int | None,
        Query(
            title="The year for which to get the schedule",
            description="The year for which to get the schedule",
            ge=MIN_YEAR_SUPPORTED,
            le=MAX_YEAR_SUPPORTED,
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


@newrelic.agent.web_transaction()
@app.get(
    "/next-event",
    tags=["schedule"],
    summary="Get upcoming event",
    response_description="Returns upcoming event",
    status_code=status.HTTP_200_OK,
    response_model=EventSchedule,
    dependencies=[Depends(validate_token)],
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
        next_event_as_json_obj: EventSchedule = EventSchedule.model_validate_json(next_event_as_json)

        return next_event_as_json_obj


@newrelic.agent.web_transaction()
@app.get(
    "/standings",
    tags=["standings"],
    summary="Get drivers and constructors standing for a given year and round",
    response_description="Return a list of drivers and constructors standings at specific points of a season for a given year and round. If the season hasn't ended you get the current standings.",
    status_code=status.HTTP_200_OK,
    response_model=Standings,
    dependencies=[Depends(validate_token)],
)
def get_standings(
    year: Annotated[
        int | None,
        Query(
            title="The year for which to get the driver and constructors standing. If the season hasn't ended you get the current standings.",
            description="The year for which to get the driver and constructors standing. If the season hasn't ended you get the current standings.",
            ge=MIN_YEAR_SUPPORTED,
            le=MAX_YEAR_SUPPORTED,
        ),
    ] = None,
    round: Annotated[
        int | None,
        Query(
            title="The round in a year for which to get the driver and constructor standings",
            description="The round in a year for which to get the driver and constructor standings",
            ge=MIN_ROUND_SUPPORTED,
            le=MAX_ROUND_SUPPORTED,
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
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong. Investigate!"
        )


@newrelic.agent.web_transaction()
@app.get(
    "/results/{year}/{round}",
    tags=["results"],
    summary="Get session results for a given year, round and session",
    response_description="Return session results for a given year, round and session.",
    status_code=status.HTTP_200_OK,
    response_model=List[Results],
    dependencies=[Depends(validate_token)],
)
def get_results(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the results",
            description="The year for which to get the results",
            ge=MIN_YEAR_SUPPORTED,
            le=MAX_YEAR_SUPPORTED,
        ),
    ],
    round: Annotated[
        int,
        Path(
            title="The round in a year for which to get the results",
            description="The round in a year for which to get the results",
            ge=MIN_ROUND_SUPPORTED,
            le=MAX_ROUND_SUPPORTED,
        ),
    ],
    session: Annotated[
        int,
        Query(
            title="The session in a round for which to get the results",
            description="The session in a round for which to get the results. (Default = 5; ie race)",
            ge=MIN_SESSION_SUPPORTED,
            le=MAX_SESSION_SUPPORTED,
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


@newrelic.agent.web_transaction()
@app.get(
    "/laps/{year}/{round}",
    tags=["laps"],
    summary="Get laps of one or more drivers for a given year, round and session",
    response_description="Return laps of one or more drivers for a given year, round and session.",
    status_code=status.HTTP_200_OK,
    response_model=List[Laps],
    dependencies=[Depends(validate_token)],
)
def get_laps(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the laps",
            description="The year for which to get the laps",
            ge=MIN_YEAR_SUPPORTED,
            le=MAX_YEAR_SUPPORTED,
        ),
    ],
    round: Annotated[
        int,
        Path(
            title="The round in a year for which to get the laps",
            description="The round in a year for which to get the laps",
            ge=MIN_ROUND_SUPPORTED,
            le=MAX_ROUND_SUPPORTED,
        ),
    ],
    session: Annotated[
        int,
        Query(
            title="The session in a round for which to get the laps",
            description="The session in a round for which to get the laps. (Default = 5; ie race)",
            ge=MIN_SESSION_SUPPORTED,
            le=MAX_SESSION_SUPPORTED,
        ),
    ] = DEFAULT_SESSION,
    driver_number: Annotated[
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
    - If no `driver_number` are provided; you get laps for all drivers.

    **Returns**:
        List[Laps]: Returns a JSON response with the list of laps
    """

    try:
        session_obj = fastf1.get_session(year=year, gp=round, identifier=session)
        session_obj.load(
            laps=True,
            telemetry=False,
            weather=False,
            messages=True,  # required for `Deleted` and `DeletedReason`
        )
        session_laps = session_obj.laps

        if len(driver_number) > 0:
            session_laps = session_laps.pick_drivers(driver_number)

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
            detail=f"Likely an error when fetching laps data for a session that has yet to happen.",
        )


@newrelic.agent.web_transaction()
@app.get(
    "/split-qualifying-laps/{year}/{round}",
    tags=["laps"],
    summary="Get split qualifying laps of one or more drivers for a given year and round",
    response_description="Return split qualifying laps of one or more drivers for a given year and round.",
    status_code=status.HTTP_200_OK,
    response_model=SplitQualifyingLaps,
    dependencies=[Depends(validate_token)],
)
def get_split_qualifying_laps(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the qualifying laps",
            description="The year for which to get the qualifying laps",
            ge=MIN_YEAR_SUPPORTED,
            le=MAX_YEAR_SUPPORTED,
        ),
    ],
    round: Annotated[
        int,
        Path(
            title="The round in a year for which to get the qualifying laps",
            description="The round in a year for which to get the qualifying laps",
            ge=MIN_ROUND_SUPPORTED,
            le=MAX_ROUND_SUPPORTED,
        ),
    ],
    driver_number: Annotated[
        List[int],
        Query(
            title="List of drivers for whom to get the qualifying laps",
            description="List of drivers for whom to get the qualifying laps",
        ),
    ] = [],
    # qualifying_session: Annotated[
    #     List[int],
    #     Query(
    #         title="List of qualifying sessions for which to get the qualifying laps",
    #         description="List of qualifying sessions for which to get the qualifying laps",
    #     ),
    # ] = [],
) -> SplitQualifyingLaps:
    """
    ## Get split qualifying laps of one or more drivers for a given year and round
    Endpoint to get split qualifying laps of one or more drivers for a given year and round.

    **NOTE**:
    - If no `driver_number` are provided; you get laps for all drivers.
    - If no `qualifying_session` are provided; you get laps for all qualifying sessions.

    **Returns**:
        SplitQualifyingLaps: Returns a JSON response with the list of split qualifying laps
    """

    # valid_qualifying_sessions = {1, 2, 3}
    # if not set(qualifying_session).issubset(valid_qualifying_sessions):
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Bad Request. Only values 1, 2, and 3 are allowed for qualifying_session.",
    #     )

    try:
        session_obj = fastf1.get_session(year=year, gp=round, identifier="Qualifying")
        session_obj.load(
            laps=True,
            telemetry=False,
            weather=False,
            messages=True,  # required for `Deleted` and `DeletedReason`
        )
        session_laps = session_obj.laps

        if len(driver_number) > 0:
            session_laps = session_laps.pick_drivers(driver_number)

        split_qualifying_laps = session_laps.split_qualifying_sessions()

        return SplitQualifyingLaps.model_validate_json(
            json.dumps(
                {
                    "Q1": (
                        None
                        if split_qualifying_laps[0] is None
                        else json.loads(split_qualifying_laps[0].to_json(orient="records"))
                    ),
                    "Q2": (
                        None
                        if split_qualifying_laps[1] is None
                        else json.loads(split_qualifying_laps[1].to_json(orient="records"))
                    ),
                    "Q3": (
                        None
                        if split_qualifying_laps[2] is None
                        else json.loads(split_qualifying_laps[2].to_json(orient="records"))
                    ),
                }
            )
        )
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request. {str(ve)}")
    except KeyError as ke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Likely an error when fetching laps data for a session that has yet to happen. {str(ke)}",
        )


@app.get(
    "/telemetry/{year}/{round}/{driver_number}/{lap}",
    tags=["telemetry"],
    summary="Get telemetry of a driver for a given year, round and session for one or multiple laps optionally with weather data",
    response_description="telemetry of a driver for a given year, round and session for one or multiple laps optionally with weather data.",
    status_code=status.HTTP_200_OK,
    response_model=ExtendedTelemetry,
    dependencies=[Depends(validate_token)],
)
def get_telemetry(
    year: Annotated[
        int,
        Path(
            title="The year for which to get the telemetry",
            description="The year for which to get the telemetry",
            ge=MIN_YEAR_SUPPORTED,
            le=MAX_YEAR_SUPPORTED,
        ),
    ],
    round: Annotated[
        int,
        Path(
            title="The round in a year for which to get the telemetry",
            description="The round in a year for which to get the telemetry",
            ge=MIN_ROUND_SUPPORTED,
            le=MAX_ROUND_SUPPORTED,
        ),
    ],
    driver_number: Annotated[
        int,
        Path(
            title="Driver number for whom to get the telemetry",
            description="Driver number for whom to get the telemetry",
            ge=MIN_DRIVER_NUMBER_SUPPORTED,
            le=MAX_DRIVER_NUMBER_SUPPORTED,
        ),
    ],
    lap: Annotated[
        int,
        Path(
            title="List of laps of the driver for which to get the telemetry",
            description="List of laps of the driver for which to get the telemetry",
            ge=MIN_LAP_COUNT_SUPPORTED,
            le=MAX_LAP_COUNT_SUPPORTED,
        ),
    ],
    session: Annotated[
        int,
        Query(
            title="The session in a round for which to get the telemetry",
            description="The session in a round for which to get the telemetry. (Default = 5; ie race)",
            ge=MIN_SESSION_SUPPORTED,
            le=MAX_SESSION_SUPPORTED,
        ),
    ] = DEFAULT_SESSION,
    weather: Annotated[
        bool,
        Query(
            title="Flag to fetch weather data along with telemetry",
            description="Flag to fetch weather data along with telemetry",
        ),
    ] = False,
) -> ExtendedTelemetry:
    """
    ## Get telemetry of a driver for a given year, round and session for one or multiple laps optionally with weather data
    Endpoint to get telemetry of a driver for a given year, round and session for one or multiple laps optionally with weather data.

    **NOTE**:
    - If `session` is not provided; we use the default session. Default = 5; ie race.

    **Returns**:
        ExtendedTelemetry: Returns a JSON response with the list of telemetry optionally with weather data
    """

    try:
        session_obj = fastf1.get_session(year=year, gp=round, identifier=session)
        session_obj.load(
            laps=True,
            telemetry=True,
            weather=weather,
            messages=True,  # required for `Deleted` and `DeletedReason`
        )
        session_laps_for_driver = session_obj.laps.pick_drivers(driver_number)
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request. {str(ve)}")
    except KeyError as ke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Likely an error when fetching laps data for a session that has yet to happen. {str(ke)}",
        )

    # Error out if no laps are found for the driver
    if len(session_laps_for_driver) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Laps for driver {driver_number} not found.",
        )

    # filter laps based on the `lap` path parameter
    filtered_lap_for_driver = session_laps_for_driver.pick_laps(lap)

    # Error out if the requested lap is not found for the driver
    if len(filtered_lap_for_driver) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Requested lap for driver {driver_number} not found.",
        )

    try:
        session_telemetry = filtered_lap_for_driver.get_telemetry()
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Telemetry not found for driver {driver_number} for the requested laps. {str(ve)}",
        )

    # keep only the required data in session_telemetry
    session_telemetry = session_telemetry[
        ["Time", "RPM", "Speed", "nGear", "Throttle", "Brake", "DRS", "Distance", "X", "Y"]
    ]

    # Convert the dataframe to a JSON string
    session_telemetry_as_json = session_telemetry.to_json(orient="records")

    # Parse the JSON string to a JSON object
    session_telemetry_as_json_obj: List[Telemetry] = json.loads(session_telemetry_as_json)

    session_weather_as_json_obj: Weather | None = None
    if weather:
        session_weather = filtered_lap_for_driver.get_weather_data()

        # Convert the dataframe to a JSON string
        session_weather_as_json = session_weather.to_json(orient="records")

        # Parse the JSON string to a JSON object
        session_weather_as_json_list_obj: List[Weather] = json.loads(session_weather_as_json)

        # Grab the first row of the weather data
        # https://docs.fastf1.dev/core.html#fastf1.core.Laps.get_weather_data
        session_weather_as_json_obj = session_weather_as_json_list_obj[0]

    return ExtendedTelemetry.model_validate(
        {
            "Telemetry": session_telemetry_as_json_obj,
            "Weather": session_weather_as_json_obj,
        }
    )
