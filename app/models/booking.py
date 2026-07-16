from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Booking(Base):
    __tablename__ = "lab_bookings"

    id = Column(Integer, primary_key=True, index=True)

    booking_date = Column(Date, nullable=False)

    department_id = Column(Integer, ForeignKey("departments.id"))

    class_id = Column(Integer, ForeignKey("classes.id"))

    lab_id = Column(Integer, ForeignKey("labs.id"))

    faculty_id = Column(Integer, ForeignKey("users.id"))

    time_slot_id = Column(Integer, ForeignKey("time_slots.id"))

    purpose = Column(String(200))

    status = Column(String(20), default="Approved")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    print("Booking model loaded")
    print("Booking has class_id only")