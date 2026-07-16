from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database_session import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.user_service import (
    get_user_by_email,
    get_all_users,
    create_user,
)
from app.auth.password import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post("/create")
def add_user(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    print(data.model_dump())

    if get_user_by_email(db, data.email):
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    user = User(
        full_name=data.full_name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role,
        department_id=data.department_id,
        class_id=data.class_id,
    )

    print(user.role)

    create_user(db, user)

    return {"message": "User Created Successfully"}

@router.get("/")
def users(
    db: Session = Depends(get_db),
):

    return get_all_users(db)