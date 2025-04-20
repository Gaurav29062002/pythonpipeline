import app

def test_add_task():
    client = app.app.test_client()
    response = client.post("/tasks", json={"title": "Learn CI/CD"})
    assert response.status_code == 201

def test_get_tasks():
    client = app.app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200

def test_delete_task():
    client = app.app.test_client()
    client.post("/tasks", json={"title": "Temp task"})
    response = client.delete("/tasks/0")
    assert response.status_code == 200
