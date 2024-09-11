from fastapi.testclient import TestClient
from frontend.main import app

client = TestClient(app)

def test_enroll_user():
    response = client.post("/users/enroll", json={
        "email": "akinyemisamuel170@gmail.com",
        "firstname": "Samuel",
        "lastname": "Akinyemi"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "akinyemisamuel170@gmail.com"