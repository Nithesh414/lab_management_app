from fastapi import FastAPI

from app.database import Base, engine

# Import all models
from app.models import *

# Routers
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.booking import router as booking_router
from app.routers.timetable import router as timetable_router
from app.routers.lab import router as lab_router
from app.routers.holiday import router as holiday_router
from app.routers.notification import router as notification_router
from app.routers.dashboard import router as dashboard_router
from app.routers.faculty_dashboard import router as faculty_dashboard_router
from app.routers import reports
from app.routers import search
from app.routers import export

# Create tables (only if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lab Management System API",
    version="1.0.0"
)

# Register Routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(booking_router)
app.include_router(timetable_router)
app.include_router(lab_router)
app.include_router(holiday_router)
app.include_router(notification_router)
app.include_router(dashboard_router)
app.include_router(faculty_dashboard_router)
app.include_router(reports.router)
app.include_router(search.router)
app.include_router(export.router)


@app.get("/")
def root():
    return {
        "status": "Running",
        "message": "Lab Management Backend Running Successfully"
    }