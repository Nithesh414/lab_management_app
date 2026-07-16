from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.reports_service import get_analytics
from app.schemas.report_schema import AnalyticsResponse

router = APIRouter(
    prefix="/reports",
    tags=["Analytics & Reports"]
)


@router.get(
    "/analytics",
    response_model=AnalyticsResponse
)
def analytics(db: Session = Depends(get_db)):
    return get_analytics(db)