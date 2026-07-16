from pydantic import BaseModel


class TimetableCreate(BaseModel):

    department_id: int

    class_id: int

    faculty_id: int

    lab_id: int

    time_slot_id: int

    day_of_week: str

    subject_code: str

    subject_name: str