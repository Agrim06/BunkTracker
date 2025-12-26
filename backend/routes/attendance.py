from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from bson import ObjectId

from database import attendance_collection, subjects_collection
from schemas.attendance import AttendanceUpdate
from deps import get_current_user
from services.attendance_service import calculate_attendance_percentage

router = APIRouter(prefix="/attendance" , tags=["Attendance"])

@router.post("/{subject_id}")
def add_attendance(
    subject_id : str,
    data : AttendanceUpdate,
    current_user : dict = Depends(get_current_user)
):
    attendance  = attendance_collection.find_one({
        "user_id" : current_user["id"],
        "subject_id" : subject_id
    })

    if not attendance :
        raise HTTPException(status_code=404 , detail="Attendance record not found")
    
    update_field = "attendance_count" if data.attended else "missed_count"

    attendance_collection.update_one(
        {"_id" : attendance["_id"]},
        {
            "$inc" : {update_field : 1},
            "$set" : {"last_updated" : datetime.utcnow()}
        }
    )

    return {"message" : "Attendance Updated!"}

@router.get("/summary" )
def attendance_summary( current_user: dict = Depends(get_current_user)):
    subjects = subjects_collection.find({"user_id" : current_user["id"]})

    summary = []

    for s in subjects:
        attendance = attendance_collection.find_one({
            "user_id"  : current_user["id"],
            "subject_id" : str(s["id"])
        })

        if not attendance:
            attended = 0
            missed = 0
        else:
            attended = attendance.get("attended_count" , 0)
            missed = attendance.get("missed_count", 0)
    
        total = attended + missed
        percentage = calculate_attendance_percentage(attended , total)

        summary.append({
            "subject_id": str(s["_id"]),
            "subject_name": s["name"],
            "attended_count": attended,
            "missed_count": missed,
            "attendance_percentage": round(percentage)
        })

    return summary