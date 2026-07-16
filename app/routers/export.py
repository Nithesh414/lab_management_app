from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.services.export_service import (
    export_bookings_csv,
    export_bookings_excel
)

router = APIRouter(
    prefix="/export",
    tags=["Export Reports"]
)


@router.get("/bookings/csv")
def export_csv(db: Session = Depends(get_db)):
    return export_bookings_csv(db)


@router.get("/bookings/excel")
def export_excel(db: Session = Depends(get_db)):
    return export_bookings_excel(db)