from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Lab(Base):
    __tablename__ = "labs"

    id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    lab_name = Column(String(100), nullable=False)
    location = Column(String(100))
    capacity = Column(Integer)