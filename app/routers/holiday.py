from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.holiday import Holiday
from app.schemas.holiday import HolidayCreate
from app.services.holiday_service import (
    create_holiday,
    get_holidays,
    delete_holiday,
)

router = APIRouter(
    prefix="/holidays",
    tags=["Holidays"],
)


@router.post("/create")
def add_holiday(
    data: HolidayCreate,
    db: Session = Depends(get_db),
):

    holiday = Holiday(**data.model_dump())

    return create_holiday(db, holiday)


@router.get("/")
def holidays(db: Session = Depends(get_db)):
    return get_holidays(db)


@router.delete("/{holiday_id}")
def remove_holiday(
    holiday_id: int,
    db: Session = Depends(get_db),
):

    holiday = delete_holiday(db, holiday_id)

    if not holiday:
        raise HTTPException(
            status_code=404,
            detail="Holiday not found",
        )

    return {"message": "Holiday deleted"}