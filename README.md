Students Register Management

A faculty stores information about:

1. Student: student_id, name
2. Discipline: discipline_id, name
3. Grade: discipline_id, student_id, grade_value
Create an application to:

Manage students and disciplines:
-The user can add, remove, update, and list both students and disciplines.
Grade students at a given discipline. Any student may receive one or several grades at any discipline. 
Deleting a student also removes their grades. Deleting a discipline deletes all grades at that discipline for all students.
Search for disciplines/students based on ID or name/title. The search must work using case-insensitive, partial string matching, and must return all matching disciplines/students.

Create statistics:
All students failing at one or more disciplines (students having an average <5 for a discipline are failing it)
Students with the best school situation, sorted in descending order of their aggregated average (the average between their average grades per discipline)

All disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline

Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying).
