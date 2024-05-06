# Built-in
from typing import Dict, List

# External
from pydantic import BaseModel, RootModel


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

    DriverNumber: str | None
    BroadcastName: str | None
    Abbreviation: str | None
    DriverId: str | None
    TeamName: str | None
    TeamColor: str | None
    TeamId: str | None
    FirstName: str | None
    LastName: str | None
    FullName: str | None
    HeadshotUrl: str | None
    CountryCode: str | None
    Position: float | None
    ClassifiedPosition: str | None
    GridPosition: float | None
    Q1: int | None
    Q2: int | None
    Q3: int | None
    Time: int | None
    Status: str | None
    Points: float | None


class Laps(BaseModel):
    """Response model for session laps for a given year, round, session and drivers"""

    Time: int | None
    Driver: str | None
    DriverNumber: str | None
    LapTime: int | None
    LapNumber: float | None
    Stint: float | None
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
    IsPersonalBest: bool | None
    Compound: str | None
    TyreLife: float | None
    FreshTyre: bool | None
    Team: str | None
    LapStartTime: int | None
    LapStartDate: str | None
    TrackStatus: str | None
    Position: float | None
    Deleted: bool | None
    DeletedReason: str | None
    FastF1Generated: bool | None
    IsAccurate: bool | None


class SplitQualifyingLaps(BaseModel):
    """Response model for split qualifying laps"""

    Q1: List[Laps] | None
    Q2: List[Laps] | None
    Q3: List[Laps] | None


class Telemetry(BaseModel):
    """Response model for session telemetry for a given year, round, session, driver and laps"""

    Time: int
    RPM: int
    Speed: float
    nGear: int
    Throttle: float
    Brake: bool
    DRS: int
    Distance: float
    X: float
    Y: float


class Weather(BaseModel):
    """Response model for session weather for a given year, round, session and laps"""

    Time: int
    AirTemp: float
    Humidity: float
    Pressure: float
    Rainfall: bool
    TrackTemp: float
    WindDirection: int
    WindSpeed: float


class ExtendedTelemetry(BaseModel):
    """Response model for telemetry with weather"""

    Telemetry: List[Telemetry]
    Weather: Weather | None


class DriverSectorTimes(BaseModel):
    MinSector1Time: float
    MinSector2Time: float
    MinSector3Time: float


class FastestSectors(RootModel):
    """Response model for fastest sectors for a given year, round and session"""

    Dict[str, DriverSectorTimes]
