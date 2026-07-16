from sqlalchemy.orm import Session
from app.models.timetable import WeeklyTimetable


def create_timetable(db: Session, timetable: WeeklyTimetable):

    db.add(timetable)

    db.commit()

    db.refresh(timetable)

    return timetable


def get_all_timetables(db: Session):

    return db.query(WeeklyTimetable).all()