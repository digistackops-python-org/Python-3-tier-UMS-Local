# backend/tests/test_unit_employees.py
from bson.objectid import ObjectId

def test_get_employees_empty(client, mocker):
    mock_collection = mocker.patch("backend.app.users_collection")
    mock_collection.find.return_value = []

    res = client.get("/api/employees")
    assert res.status_code == 200
    assert res.json == []


def test_add_employee_success(client, mocker):
    fake_id = ObjectId()

    mock_collection = mocker.patch("backend.app.users_collection")
    mock_collection.insert_one.return_value.inserted_id = fake_id
    mock_collection.find_one.return_value = {
        "_id": fake_id,
        "name": "Alice",
        "salary": 5000
    }

    res = client.post("/api/employees", json={"name": "Alice", "salary": "5000"})
    
    assert res.status_code == 201
    assert res.json["name"] == "Alice"
    assert res.json["salary"] == 5000.0
    assert "_id" in res.json


def test_add_employee_invalid_salary(client):
    res = client.post("/api/employees", json={"name": "Bob", "salary": "not-a-number"})
    assert res.status_code == 400
    assert "error" in res.json


def test_update_employee_not_found(client, mocker):
    mock_collection = mocker.patch("backend.app.users_collection")
    mock_collection.update_one.return_value.matched_count = 0

    res = client.put("/api/employees/507f1f77bcf86cd799439011", json={"salary": 3000})
    assert res.status_code == 404


def test_delete_employee_success(client, mocker):
    mock_collection = mocker.patch("backend.app.users_collection")
    mock_collection.delete_one.return_value.deleted_count = 1

    res = client.delete("/api/employees/507f1f77bcf86cd799439011")
    assert res.status_code == 200
    assert res.json["message"] == "Employee deleted successfully"
