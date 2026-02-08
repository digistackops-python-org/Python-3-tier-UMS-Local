def test_employee_full_flow(client):
    create = client.post('/api/employees', json={
        "name": "E2E",
        "email": "e2e@test.com",
        "designation": "Dev",
        "salary": 50000
    })

    emp_id = create.json['_id']

    update = client.put(f"/api/employees/{emp_id}", json={"salary": 60000})
    assert update.status_code == 200

    delete = client.delete(f"/api/employees/{emp_id}")
    assert delete.status_code == 200
