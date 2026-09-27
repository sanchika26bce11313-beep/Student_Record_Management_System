# Student Record Management System

## 1. Project Overview

The Student Record Management System is a basic Python console application designed to store and manage student information.

The project demonstrates Python programming, modular design, file handling, CRUD operations, validation, error handling, reporting, and testing.

## 2. Problem Statement

Managing student records manually can be time-consuming and can lead to duplicate, missing, or incorrectly entered information. This project provides a simple computerized system for storing and managing student records.

## 3. Objectives

- Add student records.
- View all student records.
- Search for a student.
- Update student information.
- Delete student records.
- Generate a basic marks report.
- Validate user input.
- Store data persistently using a JSON file.

## 4. Major Functional Modules

1. Student Record Management
2. Search and Update Management
3. Reporting and Analytics
4. Data Storage and Validation

## 5. Features

- Add student
- View students
- Search student
- Update student
- Delete student
- Generate report
- Input validation
- JSON file storage
- Error handling
- Unit testing

## 6. Technologies Used

- Python 3
- JSON
- Python standard library
- unittest
- Git/GitHub

No external Python packages are required.

## 7. Project Structure

```text
Student_Record_Management_System/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
├── data/
│   └── students.json
├── src/
│   ├── __init__.py
│   ├── storage.py
│   ├── validators.py
│   └── student_manager.py
├── tests/
│   └── test_student_manager.py
└── docs/
    ├── problem_statement.md
    ├── requirements.md
    ├── architecture.md
    ├── workflow.md
    ├── use_case.md
    ├── class_diagram.md
    ├── sequence_diagram.md
    ├── database_design.md
    ├── testing.md
    ├── design_decisions.md
    └── report_content.md
```

## 8. How to Run

Make sure Python 3 is installed.

Open a terminal in the project folder and run:

```bash
python main.py
```

## 9. How to Test

Run:

```bash
python -m unittest discover -s tests -v
```

## 10. Input/Output

Input:
- Student ID
- Name
- Age
- Course
- Marks

Output:
- Student records
- Search results
- Updated/deleted status
- Summary report

## 11. Data Storage

Student records are stored in `data/students.json`.

## 12. Future Enhancements

- Graphical user interface
- Login system
- SQLite/MySQL database
- Attendance management
- Export reports to CSV/PDF
- Role-based access

## 13. Academic Relevance

The project demonstrates Python programming, functions, classes, lists, dictionaries, file handling, exception handling, validation, modular programming, CRUD operations, and testing.
