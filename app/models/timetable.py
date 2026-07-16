from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class WeeklyTimetable(Base):
    __tablename__ = "weekly_timetable"

    id = Column(Integer, primary_key=True, index=True)

    department_id = Column(Integer, ForeignKey("departments.id"))

    class_id = Column(Integer, ForeignKey("classes.id"))

    faculty_id = Column(Integer, ForeignKey("users.id"))

    lab_id = Column(Integer, ForeignKey("labs.id"))

    time_slot_id = Column(Integer, ForeignKey("time_slots.id"))

    day_of_week = Column(String(15))

    subject_code = Column(String(20))

    subject_name = Column(String(100))