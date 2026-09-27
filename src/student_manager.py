from src.storage import load_students, save_students


class StudentManager:
    """Handles student CRUD operations and report generation."""

    def __init__(self):
        self.students = load_students()

    def add_student(self, student):
        if self.search_student(student["id"]):
            return False

        student["age"] = int(student["age"])
        student["marks"] = float(student["marks"])
        self.students.append(student)
        save_students(self.students)
        return True

    def get_all_students(self):
        return self.students

    def search_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None

    def update_student(self, student_id, updated_student):
        for index, student in enumerate(self.students):
            if student["id"] == student_id:
                updated_student["age"] = int(updated_student["age"])
                updated_student["marks"] = float(updated_student["marks"])
                self.students[index] = updated_student
                save_students(self.students)
                return True
        return False

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if not student:
            return False

        self.students.remove(student)
        save_students(self.students)
        return True

    def generate_report(self):
        if not self.students:
            return {
                "total": 0,
                "average_marks": 0,
                "highest_marks": 0,
                "lowest_marks": 0
            }

        marks = [float(student["marks"]) for student in self.students]
        return {
            "total": len(self.students),
            "average_marks": round(sum(marks) / len(marks), 2),
            "highest_marks": max(marks),
            "lowest_marks": min(marks)
        }
