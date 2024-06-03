import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/api/tasks",
        json={
            "title": "Test Task",
            "description": "This is a test task",
            "completed": False,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert not data["completed"]


def test_read_task():
    response = client.post(
        "/api/tasks",
        json={
            "title": "Test Task",
            "description": "This is a test task",
            "completed": False,
        },
    )
    task_id = response.json()["id"]

    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"


def test_read_tasks():
    client.post(
        "/api/tasks",
        json={"title": "Task 1", "description": "First task", "completed": False},
    )
    client.post(
        "/api/tasks",
        json={"title": "Task 2", "description": "Second task", "completed": True},
    )
    response = client.get("/api/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_update_task():
    response = client.post(
        "/api/tasks",
        json={
            "title": "Old Task",
            "description": "Old description",
            "completed": False,
        },
    )
    task_id = response.json()["id"]

    response = client.put(
        f"/api/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"
    assert data["completed"]


def test_delete_task():
    response = client.post(
        "/api/tasks",
        json={
            "title": "Task to Delete",
            "description": "This task will be deleted",
            "completed": False,
        },
    )
    task_id = response.json()["id"]

    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 204

    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "task not found."


def test_create_task_missing_data():
    response = client.post(
        "/api/tasks",
        json={"description": "Task with missing title", "completed": False},
    )
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["loc"] == ["body", "title"]
    assert data["detail"][0]["msg"] == "Field required"
