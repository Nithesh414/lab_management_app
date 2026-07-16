from sqlalchemy.orm import Session

from app.models.holiday import Holiday


def create_holiday(db: Session, holiday: Holiday):
    db.add(holiday)
    db.commit()
    db.refresh(holiday)
    return holiday


def get_holidays(db: Session):
    return db.query(Holiday).all()


def delete_holiday(db: Session, holiday_id: int):
    holiday = db.query(Holiday).filter(
        Holiday.id == holiday_id
    ).first()

    if holiday:
        db.delete(holiday)
        db.commit()

    return holiday