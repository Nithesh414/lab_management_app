from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.services.faculty_dashboard_service import (
    get_today_schedule,
    get_today_bookings,
    get_upcoming_bookings,
    get_notifications,
)

router = APIRouter(
    prefix="/faculty-dashboard",
    tags=["Faculty Dashboard"]
)


@router.get("/{faculty_id}/today-schedule")
def today_schedule(faculty_id: int, db: Session = Depends(get_db)):
    return get_today_schedule(db, faculty_id)


@router.get("/{faculty_id}/today-bookings")
def today_bookings(faculty_id: int, db: Session = Depends(get_db)):
    return get_today_bookings(db, faculty_id)


@router.get("/{faculty_id}/upcoming-bookings")
def upcoming_bookings(faculty_id: int, db: Session = Depends(get_db)):
    return get_upcoming_bookings(db, faculty_id)


@router.get("/{faculty_id}/notifications")
def notifications(faculty_id: int, db: Session = Depends(get_db)):
    return get_notifications(db, faculty_id)