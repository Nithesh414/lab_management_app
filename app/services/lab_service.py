from sqlalchemy.orm import Session
from app.models.lab import Lab
from app.models.booking import Booking


def get_available_labs(db: Session, booking_date, time_slot_id):
    booked_lab_ids = (
        db.query(Booking.lab_id)
        .filter(
            Booking.booking_date == booking_date,
            Booking.time_slot_id == time_slot_id,
        )
        .all()
    )

    booked_lab_ids = [lab[0] for lab in booked_lab_ids]

    available_labs = (
        db.query(Lab)
        .filter(~Lab.id.in_(booked_lab_ids))
        .all()
    )

    return available_labs