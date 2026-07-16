from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.lab import LabAvailabilityRequest
from app.services.lab_service import get_available_labs

router = APIRouter(
    prefix="/labs",
    tags=["Labs"],
)


@router.post("/available")
def available_labs(
    data: LabAvailabilityRequest,
    db: Session = Depends(get_db),
):
    return get_available_labs(
        db,
        data.booking_date,
        data.time_slot_id,
    )