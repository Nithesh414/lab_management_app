from datetime import datetime,date
from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.models.timetable import WeeklyTimetable
from app.models.notification import Notification
from app.models.lab import Lab
def get_today_schedule(db: Session, faculty_id: int):
    today = datetime.today().strftime("%A")

    return (
        db.query(WeeklyTimetable)
        .filter(
            WeeklyTimetable.faculty_id == faculty_id,
            WeeklyTimetable.day_of_week == today
        )
        .order_by(WeeklyTimetable.time_slot_id)
        .all()
    )
def get_today_bookings(db: Session, faculty_id: int):
    return (
        db.query(Booking)
        .filter(
            Booking.faculty_id == faculty_id,
            Booking.booking_date == date.today()
        )
        .all()
    )
def get_upcoming_bookings(db: Session, faculty_id: int):
    return (
        db.query(Booking)
        .filter(
            Booking.faculty_id == faculty_id,
            Booking.booking_date >= date.today()
        )
        .order_by(Booking.booking_date)
        .all()
    )
def get_notifications(db: Session, faculty_id: int):

    return (
        db.query(Notification)
        .filter(Notification.user_id == faculty_id)
        .order_by(Notification.created_at.desc())
        .all()
    )