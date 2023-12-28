from pydantic import BaseModel


class Schedule(BaseModel):
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
