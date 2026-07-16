from sqlalchemy import Column, Integer, String, Time, Boolean
from app.database import Base

class TimeSlot(Base):
    __tablename__ = "time_slots"

    id = Column(Integer, primary_key=True, index=True)
    hour_no = Column(Integer)
    slot_name = Column(String(30))
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    slot_type = Column(String(20))
    is_bookable = Column(Boolean, default=True)