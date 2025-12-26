
const AttendanceCard = ({ subject }) =>{
    return(
        <div className="attendance-card">
            <h3 className="attendance-title">{subject.subject_name}</h3>

            <div className="attendance-stats">
                <span>Attended: {subject.attendance_count}</span>
                <span>Missed: {subject.missed_count}</span>
            </div>

            <div className="attendance-percentage">
                {subject.attendance_percentage}%
            </div>
        </div>
    );
}; 

export default AttendanceCard;