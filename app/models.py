# Built-in
from typing import List

# External
from pydantic import BaseModel


class Root(BaseModel):
    """Response model for root"""

    we_are: str = "SlickTelemetry"


class EventSchedule(BaseModel):
    """Response model for event schedule data for a Formula 1 calendar year"""

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


class Schedule(BaseModel):
    """Response model for event schedule data with year"""

    year: int
    EventSchedule: List[EventSchedule]


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check"""

    status: str = "OK"


class Driver(BaseModel):
    """Model for driver data"""

    driverId: str
    permanentNumber: str
    code: str
    url: str
    givenName: str
    familyName: str
    dateOfBirth: str
    nationality: str


class Constructor(BaseModel):
    """Model for constructor data"""

    constructorId: str
    url: str
    name: str
    nationality: str


class DriverStandings(BaseModel):
    """Model for driver standings data"""

    position: str
    positionText: str
    points: str
    wins: str
    Driver: Driver
    Constructors: List[Constructor]


class ConstructorStandings(BaseModel):
    """Model for constructor standings data"""

    position: str
    positionText: str
    points: str
    wins: str
    Constructor: Constructor


class Standings(BaseModel):
    """Response model for driver and constructor standings for a given season and round"""

    season: int
    round: int
    DriverStandings: List[DriverStandings]
    ConstructorStandings: List[ConstructorStandings]


class Results(BaseModel):
    """Response model for session results for a given year, round and session"""

    DriverNumber: str
    BroadcastName: str
    Abbreviation: str
    DriverId: str
    TeamName: str
    TeamColor: str
    TeamId: str
    FirstName: str
    LastName: str
    FullName: str
    HeadshotUrl: str
    CountryCode: str
    Position: float | None
    ClassifiedPosition: str
    GridPosition: float | None
    Q1: int | None
    Q2: int | None
    Q3: int | None
    Time: int | None
    Status: str
    Points: float | None


class Laps(BaseModel):
    """Response model for session laps for a given year, round, session and drivers"""

    Time: int
    Driver: str
    DriverNumber: str
    LapTime: int | None
    LapNumber: float
    Stint: float
    PitOutTime: int | None
    PitInTime: int | None
    Sector1Time: int | None
    Sector2Time: int | None
    Sector3Time: int | None
    Sector1SessionTime: int | None
    Sector2SessionTime: int | None
    Sector3SessionTime: int | None
    SpeedI1: float | None
    SpeedI2: float | None
    SpeedFL: float | None
    SpeedST: float | None
    IsPersonalBest: bool
    Compound: str
    TyreLife: float
    FreshTyre: bool
    Team: str
    LapStartTime: int | None
    LapStartDate: str | None
    TrackStatus: str
    Position: float | None
    Deleted: bool | None
    DeletedReason: str
    FastF1Generated: bool
    IsAccurate: bool
