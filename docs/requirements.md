# Requirements

## Functional Requirements

### FR1 - Add Student
The system shall allow the user to add a student with ID, name, age, course, and marks.

### FR2 - View Students
The system shall display all stored student records.

### FR3 - Search Student
The system shall allow a student record to be searched using Student ID.

### FR4 - Update Student
The system shall allow an existing student's information to be modified.

### FR5 - Delete Student
The system shall allow an existing student record to be deleted.

### FR6 - Generate Report
The system shall calculate total students, average marks, highest marks, and lowest marks.

## Non-Functional Requirements

### NFR1 - Usability
The menu and messages should be simple enough for a beginner to understand.

### NFR2 - Reliability
Records should be saved to persistent storage after changes.

### NFR3 - Maintainability
The program should be divided into meaningful modules.

### NFR4 - Error Handling
Invalid age, marks, empty fields, duplicate IDs, and invalid menu choices should be handled.

### NFR5 - Resource Efficiency
The application should use only lightweight local JSON storage and Python standard-library functionality.
