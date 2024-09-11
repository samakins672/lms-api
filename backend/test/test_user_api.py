from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_add_book():
    response = client.post("/admin/books", json={
        "id": 1,
        "title": "Python Programming",
        "author": "John Smith",
        "publisher": "Wiley",
        "category": "Technology"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Book added successfully"
