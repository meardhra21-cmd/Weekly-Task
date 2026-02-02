attendance = []


def mark_attendance():
    day = input("Enter attendance (P/A): ")
    attendance.append(day)


def calculate_working_days():
    present_days = attendance.count("P")
    return present_days


def generate_report():
    print("\n--- Attendance Report ---")
    print("Total Days:", len(attendance))
    print("Present Days:", calculate_working_days())
    print("Absent Days:", attendance.count("A"))


mark_attendance()
mark_attendance()
mark_attendance()

generate_report()
