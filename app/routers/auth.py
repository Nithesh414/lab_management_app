from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database_session import get_db
from app.services.user_service import get_user_by_email
from app.auth.password import verify_password
from app.schemas.auth import LoginRequest
from app.auth.jwt_handler import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(data: LoginRequest):

    if data.email == "admin@gmail.com" and data.password == "admin123":

        token = create_access_token({
            "email": data.email,
            "role": "admin"
        })

        return {
            "access_token": token,
            "token_type": "bearer",
            "role": "admin"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid Credentials"
    )
    user = get_user_by_email(db, data.email)

    if user is None:
        raise HTTPException(
        status_code=401,
        detail="Invalid Email"
    )

    if not verify_password(data.password, user.password):
        raise HTTPException(
        status_code=401,
        detail="Wrong Password"
    )

    token = create_access_token(
        {
        "id": user.id,
        "role": user.role,
        "email": user.email
        }
    )

    return {
    "access_token": token,
    "token_type": "bearer",
    "role": user.role
    }