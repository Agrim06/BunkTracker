
const AttendanceCard = ({ subject }) =>{
    let status = "SAFE";
    let statusClass = "status-safe";

    if(subject.attendance_percentage < 75){
        status = "SHORTAGE";
        statusClass = "status-danger";
    }else if(subject.safe_bunk === 0){
        status = "BORDERLINE";
        statusClass = "status-warning"
    }


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

            <div className="attendance-bunk">
                Safe bunks left: <strong>{subject.safe_bunk}</strong>
            </div>

            <div className={`attendance-status ${statusClass}`}>
                {status}
            </div>
        </div>
        );
    };

export default AttendanceCard;
