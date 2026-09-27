# Testing Approach

The project uses Python's built-in `unittest` framework.

## Test Cases

| Test | Expected Result |
|---|---|
| Add valid student | Student is stored |
| Add duplicate ID | Operation rejected |
| Search existing student | Correct record returned |
| Update student | Updated values are stored |
| Delete student | Record is removed |
| Generate report | Correct statistics are returned |

Run tests with:

```bash
python -m unittest discover -s tests -v
```
