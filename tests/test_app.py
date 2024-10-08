import sys
import os
from app import app
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_ask_endpoint(client):
    # Simulate a POST request to the /ask endpoint
    response = client.post('/ask', json={'question': 'What is AI?'})

    # Check the response status code
    assert response.status_code == 200

    # Check if the response contains an answer
    data = response.get_json()
    assert 'answer' in data
    assert isinstance(data['answer'], str)  # Ensure that 'answer' is a string
    assert len(data['answer']) > 0  # Ensure that the answer is not empty
