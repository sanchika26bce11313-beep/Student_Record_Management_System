from src.student_manager import StudentManager
from src.validators import validate_student

manager = StudentManager()


def menu():
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Report")
    print("7. Exit")


def add_student():
    student_id = input("Student ID: ").strip()
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    course = input("Course: ").strip()
    marks = input("Marks (0-100): ").strip()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    valid, message = validate_student(student)
    if not valid:
        print("Error:", message)
        return

    if manager.add_student(student):
        print("Student added successfully.")
    else:
        print("Error: Student ID already exists.")


def view_students():
    students = manager.get_all_students()
    if not students:
        print("No student records found.")
        return

    print("\nID | Name | Age | Course | Marks")
    print("-" * 45)
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['age']} | {s['course']} | {s['marks']}")


def search_student():
    student_id = input("Enter Student ID: ").strip()
    student = manager.search_student(student_id)

    if student:
        print("\nStudent Found")
        for key, value in student.items():
            print(f"{key.title()}: {value}")
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ").strip()
    student = manager.search_student(student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")
    name = input(f"Name [{student['name']}]: ").strip() or student["name"]
    age = input(f"Age [{student['age']}]: ").strip() or student["age"]
    course = input(f"Course [{student['course']}]: ").strip() or student["course"]
    marks = input(f"Marks [{student['marks']}]: ").strip() or student["marks"]

    updated = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    valid, message = validate_student(updated)
    if not valid:
        print("Error:", message)
        return

    manager.update_student(student_id, updated)
    print("Student updated successfully.")


def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    if manager.delete_student(student_id):
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def report():
    stats = manager.generate_report()
    print("\n===== REPORT =====")
    print("Total students:", stats["total"])
    print("Average marks:", stats["average_marks"])
    print("Highest marks:", stats["highest_marks"])
    print("Lowest marks:", stats["lowest_marks"])


def main():
    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            report()
        elif choice == "7":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
