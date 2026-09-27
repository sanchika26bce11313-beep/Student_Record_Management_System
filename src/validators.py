def validate_student(student):
    if not student["id"]:
        return False, "Student ID cannot be empty."

    if not student["name"]:
        return False, "Name cannot be empty."

    try:
        age = int(student["age"])
    except ValueError:
        return False, "Age must be a whole number."

    if age < 1 or age > 100:
        return False, "Age must be between 1 and 100."

    if not student["course"]:
        return False, "Course cannot be empty."

    try:
        marks = float(student["marks"])
    except ValueError:
        return False, "Marks must be a number."

    if marks < 0 or marks > 100:
        return False, "Marks must be between 0 and 100."

    return True, "Valid"
