import json

def test_salary_validation(client):
    res = client.post('/api/employees', json={
        "name": "Test",
        "salary": "abc"
    })
    assert res.status_code == 400
