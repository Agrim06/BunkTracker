from pydantic import BaseModel

class AttendanceUpdate(BaseModel):
    attended: bool  

class AttendanceSummary(BaseModel):
    subject_id: int
    subject_name: str
    attended_count: int
    missed_count: int
    attendance_percentage: float
