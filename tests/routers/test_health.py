from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/tasks/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
