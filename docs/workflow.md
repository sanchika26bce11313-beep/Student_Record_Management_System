# Workflow Diagram

```text
START
  |
  v
Display Menu
  |
  v
Choose Operation
  |
  +---- Add ----> Validate Input ----> Save Record
  |
  +---- View ---> Load Records -----> Display Records
  |
  +---- Search -> Find ID ----------> Display Result
  |
  +---- Update -> Find ID ----------> Validate ----> Save
  |
  +---- Delete -> Find ID ----------> Remove -----> Save
  |
  +---- Report -> Calculate Statistics -> Display Report
  |
  +---- Exit ------------------------> END
  |
  v
Return to Menu
```
