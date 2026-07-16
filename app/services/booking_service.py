from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models.booking import Booking


def create_booking(db: Session, booking: Booking):

    existing = db.query(Booking).filter(
        Booking.lab_id == booking.lab_id,
        Booking.booking_date == booking.booking_date,
        Booking.time_slot_id == booking.time_slot_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Lab already booked for this time slot."
        )

    try:
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Lab already booked."
        )