from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.timetable import WeeklyTimetable
from app.schemas.timetable import TimetableCreate
from app.services.timetable_service import (
    create_timetable,
    get_all_timetables,
)

router = APIRouter(
    prefix="/timetable",
    tags=["Timetable"],
)


@router.post("/create")
def add_timetable(
    data: TimetableCreate,
    db: Session = Depends(get_db),
):

    timetable = WeeklyTimetable(**data.model_dump())

    return create_timetable(db, timetable)


@router.get("/")
def view_timetable(
    db: Session = Depends(get_db),
):

    return get_all_timetables(db)