from pydantic import BaseModel


class AdminDashboard(BaseModel):
    total_departments: int
    total_labs: int
    total_faculties: int
    total_classes: int
    total_bookings: int
    pending_bookings: int
    approved_bookings: int
    rejected_bookings: int
    holidays: int
class FacultyDashboard(BaseModel):
    my_bookings: int
    pending: int
    approved: int
    rejected: int
    unread_notifications: int
class HodDashboard(BaseModel):
    department_name: str
    total_faculties: int
    total_classes: int
    total_labs: int
    total_bookings: int
    pending_bookings: int
    approved_bookings: int
    rejected_bookings: int
class DashboardResponse(BaseModel):
    total_departments: int
    total_classes: int
    total_faculties: int
    total_labs: int
    today_bookings: int
    upcoming_bookings: int
    today_holidays: int
    available_labs: int