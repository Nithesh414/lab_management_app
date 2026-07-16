from datetime import date
from sqlalchemy.orm import Session
from app.models.department import Department
from app.models.lab import Lab
from app.models.user import User
from app.models.class_model import Class
from app.models.booking import Booking
from app.models.holiday import Holiday
from app.models.notification import Notification
from app.models.department import Department
def admin_dashboard(db: Session):
    return {
        "total_departments": db.query(Department).count(),
        "total_labs": db.query(Lab).count(),
        "total_faculties": db.query(User).filter(User.role == "Faculty").count(),
        "total_classes": db.query(Class).count(),
        "total_bookings": db.query(Booking).count(),
        "pending_bookings": db.query(Booking).filter(Booking.status == "Pending").count(),
        "approved_bookings": db.query(Booking).filter(Booking.status == "Approved").count(),
        "rejected_bookings": db.query(Booking).filter(Booking.status == "Rejected").count(),
        "holidays": db.query(Holiday).count()
    }
def faculty_dashboard(db: Session, faculty_id: int):
    return {
        "my_bookings": db.query(Booking).filter(
            Booking.faculty_id == faculty_id
        ).count(),

        "pending": db.query(Booking).filter(
            Booking.faculty_id == faculty_id,
            Booking.status == "Pending"
        ).count(),

        "approved": db.query(Booking).filter(
            Booking.faculty_id == faculty_id,
            Booking.status == "Approved"
        ).count(),

        "rejected": db.query(Booking).filter(
            Booking.faculty_id == faculty_id,
            Booking.status == "Rejected"
        ).count(),

        "unread_notifications": db.query(Notification).filter(
            Notification.user_id == faculty_id,
            Notification.is_read == False
        ).count()
    }
def hod_dashboard(db: Session, department_id: int):

    department = db.query(Department).filter(
        Department.id == department_id
    ).first()

    return {
        "department_name": department.department_name if department else "Unknown",

        "total_faculties": db.query(User).filter(
            User.department_id == department_id,
            User.role == "Faculty"
        ).count(),

        "total_classes": db.query(Class).filter(
            Class.department_id == department_id
        ).count(),

        "total_labs": db.query(Lab).filter(
            Lab.department_id == department_id
        ).count(),

        "total_bookings": db.query(Booking).filter(
            Booking.department_id == department_id
        ).count(),

        "pending_bookings": db.query(Booking).filter(
            Booking.department_id == department_id,
            Booking.status == "Pending"
        ).count(),

        "approved_bookings": db.query(Booking).filter(
            Booking.department_id == department_id,
            Booking.status == "Approved"
        ).count(),

        "rejected_bookings": db.query(Booking).filter(
            Booking.department_id == department_id,
            Booking.status == "Rejected"
        ).count()
    }

def get_dashboard_data(db: Session):

    total_departments = db.query(Department).count()

    total_classes = db.query(Class).count()

    total_faculties = (
        db.query(User)
        .filter(User.role == "Faculty")
        .count()
    )

    total_labs = db.query(Lab).count()

    today_bookings = (
        db.query(Booking)
        .filter(Booking.booking_date == date.today())
        .count()
    )

    upcoming_bookings = (
        db.query(Booking)
        .filter(Booking.booking_date >= date.today())
        .count()
    )

    today_holidays = (
        db.query(Holiday)
        .filter(Holiday.holiday_date == date.today())
        .count()
    )

    booked_labs = (
    db.query(Booking.lab_id)
    .filter(Booking.booking_date == date.today())
    .distinct()
    .count())
    available_labs = total_labs - booked_labs

    return {
        "total_departments": total_departments,
        "total_classes": total_classes,
        "total_faculties": total_faculties,
        "total_labs": total_labs,
        "available_labs": available_labs,
        "today_bookings": today_bookings,
        "upcoming_bookings": upcoming_bookings,
        "today_holidays": today_holidays,
    }