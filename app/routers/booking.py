from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.booking import Booking

from app.schemas.booking import BookingCreate

from app.services.booking_service import create_booking
from app.models.booking import Booking

print("Booking imported from:")
print(Booking.__module__)
print(Booking.__table__.columns.keys())
router = APIRouter(prefix="/booking", tags=["Booking"])

@router.post(
    "/create",
    responses={
        400: {
            "description": "Duplicate booking",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Lab already booked for this time slot."
                    }
                }
            },
        },
    },
)
def add_booking(data: BookingCreate, db: Session = Depends(get_db)):
    print(data.model_dump())

    booking = Booking(**data.model_dump())

    print(booking.__dict__)

    return create_booking(db, booking)