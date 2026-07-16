from sqlalchemy.orm import Session
from app.models.notification import Notification
from fastapi import HTTPException

def create_notification(db: Session, data):
    obj = Notification(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_notifications(db: Session, user_id: int):
    return (
        db.query(Notification)
        .filter(Notification.user_id == user_id)
        .order_by(Notification.created_at.desc())
        .all()
    )

def mark_as_read(db: Session, notification_id: int):
    notification = (
        db.query(Notification)
        .filter(Notification.id == notification_id)
        .first()
    )

    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    notification.is_read = True

    db.commit()
    db.refresh(notification)

    return notification