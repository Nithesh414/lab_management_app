from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.dashboard import HodDashboard
from app.services.dashboard_service import hod_dashboard
from app.database import get_db
from app.services.dashboard_service import admin_dashboard
from app.schemas.dashboard import AdminDashboard
from app.schemas.dashboard import FacultyDashboard
from app.services.dashboard_service import faculty_dashboard
from app.services.dashboard_service import get_dashboard_data
router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/admin", response_model=AdminDashboard)
def admin(db: Session = Depends(get_db)):
    return admin_dashboard(db)

@router.get(
    "/faculty/{faculty_id}",
    response_model=FacultyDashboard
)
def faculty_dashboard_api(
    faculty_id: int,
    db: Session = Depends(get_db),
):
    return faculty_dashboard(db, faculty_id)
@router.get(
    "/hod/{department_id}",
    response_model=HodDashboard
)
def hod_dashboard_api(
    department_id: int,
    db: Session = Depends(get_db)
):
    return hod_dashboard(db, department_id)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    return get_dashboard_data(db)