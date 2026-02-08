def test_get_employees_real_db(client_integration):
    response = client_integration.get("/api/employees")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_add_and_delete_employee(client_integration):
    payload = {
        "name": "Integration User",
        "email": "integration@sapsecops.com",
        "designation": "DevOps",
        "salary": 200000
    }

    # ADD
    add_resp = client_integration.post("/api/employees", json=payload)
    assert add_resp.status_code == 201
    emp_id = add_resp.json["_id"]

    # DELETE
    del_resp = client_integration.delete(f"/api/employees/{emp_id}")
    assert del_resp.status_code == 200


def test_update_employee_not_found(client_integration):
    response = client_integration.put(
        "/api/employees/65f000000000000000000000",
        json={"designation": "Manager"}
    )
    assert response.status_code == 404