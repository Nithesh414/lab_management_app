from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    total_departments: int
    total_classes: int
    total_faculties: int
    total_labs: int

    total_bookings: int
    today_bookings: int
    upcoming_bookings: int

    available_labs: int

    total_holidays: int
    today_holidays: int