import {useState, useEffect} from "react";
import { getAttendanceSummary } from "../api/attendance.api";
import AttendanceCard from "../components/attendance/AttendanceCard"

const Dashboard = () =>{
    const [summary , setSummary] = useState([]);
    const [loading , setLoading] = useState(true);
    const [error , setError] = useState("");

    useEffect(() =>{
        getAttendanceSummary()
            .then((data) => {
                setSummary(data);
                setLoading(false)
            })
            .catch(() =>{
                setError("Failed to load attendance summary")
                setLoading(false)
            });
         }, [])

    if (loading) return <p> Loading... </p>
    if (error) return <p> Error... </p>

    return (
        <div className="dashboard">
            <h1 className="dashboard-title">Attendance Overview</h1>

            <div className="attendance-grid">
                {summary.map((subject) => (
                <AttendanceCard
                    key={subject.subject_id}
                    subject={subject}
                />
                ))}
            </div>
        </div>
         );
    };

    export default Dashboard;
