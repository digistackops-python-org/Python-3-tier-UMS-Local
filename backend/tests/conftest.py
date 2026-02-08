# backend/tests/conftest.py
import pytest
from app import create_app
import mongomock

@pytest.fixture
def client_unit():
    """Unit test client with mocked MongoDB"""
    mongo_client = mongomock.MongoClient()
    mongo_uri = "mongodb://localhost"
    app = create_app(testing=True, mongo_uri=mongo_uri)
    app.testing = True
    return app.test_client()


@pytest.fixture
def client_integration():
    """Integration test client with REAL MongoDB"""
    mongo_uri = "mongodb://appuser:Pa55Word@localhost:27017/user-account"
    app = create_app(testing=True, mongo_uri=mongo_uri)
    app.testing = True
    return app.test_client()
