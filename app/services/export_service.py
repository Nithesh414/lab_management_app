import io
import pandas as pd

from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse

from app.models.booking import Booking


def export_bookings_csv(db: Session):

    bookings = db.query(Booking).all()

    data = []

    for booking in bookings:
        data.append({
            "Booking ID": booking.id,
            "Booking Date": booking.booking_date,
            "Faculty ID": booking.faculty_id,
            "Department ID": booking.department_id,
            "Class ID": booking.class_id,
            "Lab ID": booking.lab_id,
            "Time Slot": booking.time_slot_id,
            "Purpose": booking.purpose,
            "Status": booking.status
        })

    df = pd.DataFrame(data)

    output = io.StringIO()

    df.to_csv(output, index=False)

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=lab_bookings.csv"
        }
    )


def export_bookings_excel(db: Session):

    bookings = db.query(Booking).all()

    data = []

    for booking in bookings:
        data.append({
            "Booking ID": booking.id,
            "Booking Date": booking.booking_date,
            "Faculty ID": booking.faculty_id,
            "Department ID": booking.department_id,
            "Class ID": booking.class_id,
            "Lab ID": booking.lab_id,
            "Time Slot": booking.time_slot_id,
            "Purpose": booking.purpose,
            "Status": booking.status
        })

    df = pd.DataFrame(data)

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition":
            "attachment; filename=lab_bookings.xlsx"
        }
    )