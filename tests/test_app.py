import pytest
from app.app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health(client):
    # Test obligatoire /healthz [cite: 129]
    res = client.get('/healthz')
    assert res.status_code == 200
    assert res.json['status'] == 'healthy' [cite: 134]

def test_api_events(client):
    # Test obligatoire structure stable [cite: 143]
    res = client.get('/api/events')
    assert res.status_code == 200
    assert 'items' in res.json