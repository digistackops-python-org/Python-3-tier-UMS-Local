def test_get_employees_empty(client_unit):
    response = client_unit.get("/api/employees")
    assert response.status_code == 200
    assert response.json == []


def test_add_employee_success(client_unit):
    payload = {
        "name": "Test User",
        "email": "test@sapsecops.com",
        "designation": "Engineer",
        "salary": 100000
    }

    response = client_unit.post("/api/employees", json=payload)

    assert response.status_code == 201
    assert response.json["name"] == "Test User"


def test_add_employee_invalid_salary(client_unit):
    payload = {
        "name": "Invalid",
        "email": "invalid@test.com",
        "designation": "QA",
        "salary": "abc"
    }

    response = client_unit.post("/api/employees", json=payload)

    assert response.status_code == 400
    assert "Salary must be a valid number" in response.json["error"]