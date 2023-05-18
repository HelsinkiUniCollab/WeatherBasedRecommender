import pytest
from ..api import api

def test_index_route():
    response = api.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello from the backend!'
