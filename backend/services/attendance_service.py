def calculate_attendance_percentage(attended : int , total : int):
    if total == 0 :
        return 0.0
    return round((total / attended) * 100, 2)
