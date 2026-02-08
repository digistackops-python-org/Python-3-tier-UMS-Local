def test_create_and_get_employee(client):
    payload = {
        "name": "Integration User",
        "email": "test@test.com",
        "designation": "QA",
        "salary": 90000
    }

    res = client.post('/api/employees', json=payload)
    assert res.status_code == 201

    res = client.get('/api/employees')
    assert res.status_code == 200
    assert len(res.json) > 0
