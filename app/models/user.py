from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String)

    email = Column(String, unique=True)

    password = Column(String)

    role = Column(String)

    department_id = Column(Integer)

    class_id = Column(Integer, nullable=True)