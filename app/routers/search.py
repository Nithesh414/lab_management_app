from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.services.search_service import (
    search_lab_by_name,
    search_faculty_by_name,
    search_department_by_name,
)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/labs")
def search_labs(name: str, db: Session = Depends(get_db)):
    return search_lab_by_name(db, name)


@router.get("/faculty")
def search_faculty(name: str, db: Session = Depends(get_db)):
    return search_faculty_by_name(db, name)


@router.get("/departments")
def search_departments(name: str, db: Session = Depends(get_db)):
    return search_department_by_name(db, name)