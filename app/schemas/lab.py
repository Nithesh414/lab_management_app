from pydantic import BaseModel
from datetime import date


class LabAvailabilityRequest(BaseModel):
    booking_date: date
    time_slot_id: int


class LabResponse(BaseModel):
    id: int
    lab_name: str

    class Config:
        from_attributes = True