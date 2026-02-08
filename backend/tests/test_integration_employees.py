# backend/tests/test_integration_employees.py
import os
import pytest
from backend.app import app, users_collection
from bson.objectid import ObjectId

@pytest.fixture(autouse=True)
def clean_db():
    users_collection.delete_many({})
    yield
    users_collection.delete_many({})


def test_full_employee_flow(client):
    # Create
    res = client.post("/api/employees", json={
        "name": "Integration User",
        "salary": 4000
    })
    assert res.status_code == 201
    emp_id = res.json["_id"]

    # Read
    res = client.get("/api/employees")
    assert res.status_code == 200
    assert len(res.json) == 1

    # Update
    res = client.put(f"/api/employees/{emp_id}", json={
        "salary": 9999
    })
    assert res.status_code == 200

    # Delete
    res = client.delete(f"/api/employees/{emp_id}")
    assert res.status_code == 200

    # Confirm deletion
    res = client.get("/api/employees")
    assert res.json == []
