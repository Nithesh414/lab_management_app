from sqlalchemy.orm import Session

from app.models.lab import Lab
from app.models.user import User
from app.models.department import Department


def search_lab_by_name(db: Session, name: str):
    return (
        db.query(Lab)
        .filter(Lab.lab_name.ilike(f"%{name}%"))
        .all()
    )


def search_faculty_by_name(db: Session, name: str):
    return (
        db.query(User)
        .filter(
        User.role.ilike("faculty"),
        User.full_name.ilike(f"%{name}%"))
        .all()
    )

def search_department_by_name(db: Session, name: str):
    return (
        db.query(Department)
        .filter(
            (Department.department_name.ilike(f"%{name}%")) |
            (Department.department_code.ilike(f"%{name}%"))
        )
        .all()
    )