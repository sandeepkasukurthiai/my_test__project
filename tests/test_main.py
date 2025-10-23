
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI student project!"}

def test_add_and_list_students():
    # Add a student
    student = {"id": 1, "name": "Alice", "age": 20, "grade": "A"}
    response = client.post("/students", json=student)
    assert response.status_code == 200
    assert response.json() == student
    # List students
    response = client.get("/students")
    assert response.status_code == 200
    assert student in response.json()

def test_get_student():
    student = {"id": 2, "name": "Bob", "age": 21, "grade": "B"}
    client.post("/students", json=student)
    response = client.get(f"/students/{student['id']}")
    assert response.status_code == 200
    assert response.json() == student

def test_delete_student():
    student = {"id": 3, "name": "Charlie", "age": 22, "grade": "C"}
    client.post("/students", json=student)
    response = client.delete(f"/students/{student['id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Student deleted"
    # Confirm deletion
    response = client.get(f"/students/{student['id']}")
    assert response.status_code == 404
