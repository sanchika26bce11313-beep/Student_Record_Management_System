# System Architecture

The project follows a simple layered architecture.

```text
+----------------------+
|        User          |
+----------+-----------+
           |
           v
+----------------------+
|      main.py         |
|  Console Interface   |
+----------+-----------+
           |
           v
+----------------------+
|  StudentManager      |
| Business Operations  |
+----------+-----------+
           |
     +-----+------+
     |            |
     v            v
+---------+  +-------------+
|Validator|  |  Storage    |
+---------+  +------+------+
                    |
                    v
             students.json
```

## Layers

1. Presentation layer: `main.py`
2. Business logic: `student_manager.py`
3. Validation: `validators.py`
4. Storage: `storage.py`
5. Data file: `students.json`
