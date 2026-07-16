from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.notification import (
    NotificationCreate,
    NotificationResponse,
)
from app.services.notification_service import (
    create_notification,
    get_notifications,
    mark_as_read,
)

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post("/", response_model=NotificationResponse)
def add_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
):
    return create_notification(db, notification)


@router.get("/{user_id}", response_model=list[NotificationResponse])
def list_notifications(
    user_id: int,
    db: Session = Depends(get_db),
):
    return get_notifications(db, user_id)

@router.put(
    "/{notification_id}/read",
    response_model=NotificationResponse
)
def read_notification(
    notification_id: int,
    db: Session = Depends(get_db),
):
    return mark_as_read(db, notification_id)