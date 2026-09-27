# Storage Design

This project does not use a relational database. It uses a JSON file because the project is intentionally simple and requires no external packages.

File:

`data/students.json`

Each student is stored as:

```json
{
    "id": "101",
    "name": "Aarav",
    "age": 19,
    "course": "Python",
    "marks": 85.0
}
```

## Logical Fields

| Field | Type | Description |
|---|---|---|
| id | String | Unique student identifier |
| name | String | Student name |
| age | Integer | Student age |
| course | String | Course name |
| marks | Number | Marks from 0 to 100 |
