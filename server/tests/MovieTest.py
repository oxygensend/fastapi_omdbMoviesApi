from email import header
from http import client
from pydoc import cli
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_add_movie():
    response = client.post('/movies', json={
        "title": "The Fast and The Furious",
        "year": 2001
    });

    assert response.status_code == 200