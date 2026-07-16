from datetime import date
from pydantic import BaseModel

class HolidayCreate(BaseModel):
    holiday_date: date
    title: str


class HolidayResponse(HolidayCreate):
    id: int

    class Config:
        from_attributes = True