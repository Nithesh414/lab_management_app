from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    class_name = Column(String(50), nullable=False)