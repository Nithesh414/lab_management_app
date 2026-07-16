from pydantic import BaseModel
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: int
    message: str


class NotificationResponse(NotificationCreate):
    id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True