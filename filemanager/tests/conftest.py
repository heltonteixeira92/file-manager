import pytest
from fastapi.testclient import TestClient

from filemanager.app import app


@pytest.fixture
def client():
    return TestClient(app)
