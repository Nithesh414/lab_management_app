from pydantic import BaseModel


class TimetableCreate(BaseModel):
    day_of_week: str
    lab_id: int
    class_id: int
    faculty_id: int
    time_slot_id: int
    subject_name: str


class TimetableResponse(TimetableCreate):
    id: int

    class Config:
        from_attributes = True