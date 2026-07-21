#Activity 2: Aliah's Cafeteria Queue Assistant

def check_fast_lane(minutes_left, items, teacher_pass):
    if teacher_pass:
        return "Fast lane approved"
    elif minutes_left < 10 and items <= 3:
        return "Fast lane approved"
    else:
        return "Use regular line"


# Sample data
students_in_line = [
    {"name": "Marco", "minutes_left": 8, "items": 2, "teacher_pass": False},
    {"name": "Diane", "minutes_left": 15, "items": 1, "teacher_pass": False},
    {"name": "Kyle", "minutes_left": 5, "items": 6, "teacher_pass": False},
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
]


fast_lane_count = 0
print("=Cafeteria Fast Lane Status =\n")


for student in students_in_line:
    result = check_fast_lane(
        student["minutes_left"], 
        student["items"], 
        student["teacher_pass"]
    )

    if result == "Fast lane approved":
        fast_lane_count += 1
        print(student['name'] + ": " + result)
    else:
        # Rule: Inform student of remaining time and suggest regular line
        print(student['name'] + ": " + result + " (You have " + str(student['minutes_left']) + " minutes left)")


print("\n================================")
print("Total students approved for Fast Lane: " + str(fast_lane_count))