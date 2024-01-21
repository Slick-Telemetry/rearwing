from pydantic import BaseModel


class ReadRoot(BaseModel):
    """Response model to validate and return when performing a health check."""

    we_are: str = "SlickTelemetry"


class Schedule(BaseModel):
    """Response model for schedule data for a Formula 1 calendar year."""

    RoundNumber: int
    Country: str
    Location: str
    OfficialEventName: str
    EventDate: str
    EventName: str
    EventFormat: str
    Session1: str
    Session1Date: str
    Session1DateUtc: str
    Session2: str
    Session2Date: str
    Session2DateUtc: str
    Session3: str
    Session3Date: str
    Session3DateUtc: str
    Session4: str
    Session4Date: str
    Session4DateUtc: str
    Session5: str
    Session5Date: str
    Session5DateUtc: str
    F1ApiSupport: bool


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


class Driver(BaseModel):
    """Model for storing driver data"""

    driverId: str
    permanentNumber: str
    code: str
    url: str
    givenName: str
    familyName: str
    dateOfBirth: str
    nationality: str


class Contructor(BaseModel):
    """Model for storing constructor data"""

    constructorId: str
    url: str
    name: str
    nationality: str


class DriverStandings(BaseModel):
    """Model for storing driver standings data"""

    position: str
    positionText: str
    points: str
    wins: str
    Driver: Driver
    Constructors: list[Contructor]


class ConstructorStandings(BaseModel):
    """Model for storing constructor standings data"""

    position: str
    positionText: str
    points: str
    wins: str
    Constructor: Contructor


class Standings(BaseModel):
    """Response model for driver and contructor standings for a given season and round"""

    season: int
    round: int
    DriverStandings: list[DriverStandings]
    ConstructorStandings: list[ConstructorStandings]
