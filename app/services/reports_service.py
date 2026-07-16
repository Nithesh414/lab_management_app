from datetime import date
from sqlalchemy.orm import Session

from app.models.department import Department
from app.models.class_model import Class
from app.models.user import User
from app.models.lab import Lab
from app.models.booking import Booking
from app.models.holiday import Holiday


def get_analytics(db: Session):

    total_departments = db.query(Department).count()

    total_classes = db.query(Class).count()

    total_faculties = (
        db.query(User)
        .filter(User.role == "faculty")
        .count()
    )

    total_labs = db.query(Lab).count()

    total_bookings = db.query(Booking).count()

    today_bookings = (
        db.query(Booking)
        .filter(
            Booking.booking_date == date.today()
        )
        .count()
    )

    upcoming_bookings = (
        db.query(Booking)
        .filter(
            Booking.booking_date >= date.today()
        )
        .count()
    )

    total_holidays = db.query(Holiday).count()

    today_holidays = (
        db.query(Holiday)
        .filter(
            Holiday.holiday_date == date.today()
        )
        .count()
    )

    available_labs = max(0, total_labs - today_bookings)

    return {
        "total_departments": total_departments,
        "total_classes": total_classes,
        "total_faculties": total_faculties,
        "total_labs": total_labs,

        "total_bookings": total_bookings,
        "today_bookings": today_bookings,
        "upcoming_bookings": upcoming_bookings,

        "available_labs": available_labs,

        "total_holidays": total_holidays,
        "today_holidays": today_holidays,
    }