from pydantic import BaseModel
from datetime import date


class BookingCreate(BaseModel):

    booking_date: date

    department_id: int

    class_id: int

    lab_id: int

    faculty_id: int

    time_slot_id: int

    purpose: str