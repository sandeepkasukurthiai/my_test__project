
# This is first API program
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory student store
students = {}

class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI student project!"}

# 1. List all students
@app.get("/students")
def list_students():
    return list(students.values())

# 2. Get a student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = students.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# 3. Add a new student
@app.post("/students")
def add_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    students[student.id] = student.dict()
    return student

# 4. Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"detail": "Student deleted"}
