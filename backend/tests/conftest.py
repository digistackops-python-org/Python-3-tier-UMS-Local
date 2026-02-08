import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app(testing=True, mongo_uri="mongodb://localhost:27017")
    app.testing = True
    with app.test_client() as client:
        yield client