# Class Diagram

```text
+--------------------------------+
|        StudentManager          |
+--------------------------------+
| - students                     |
+--------------------------------+
| + add_student(student)         |
| + get_all_students()           |
| + search_student(student_id)   |
| + update_student(id, student)  |
| + delete_student(student_id)   |
| + generate_report()            |
+--------------------------------+

Uses:

+-------------------------+
|       Storage           |
+-------------------------+
| load_students()         |
| save_students()         |
+-------------------------+

+-------------------------+
|       Validator         |
+-------------------------+
| validate_student()      |
+-------------------------+
```
