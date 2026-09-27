# Sequence Diagram - Add Student

```text
User        main.py       Validator      StudentManager       Storage
 |             |              |                |                |
 |--input----->|              |                |                |
 |             |--validate--->|                |                |
 |             |<--valid------|                |                |
 |             |----------------add_student--->|                |
 |             |                               |--save--------->|
 |             |                               |<--success------|
 |<--message---|                               |                |
```

This sequence shows how a new student record moves through the application.
