# test_main.py

import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_valid_query():
    response = client.post(
        "/question/", json={"text": "Artificial Intelligence"})
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert isinstance(data["result"], list)
    assert len(data["result"]) > 0
    assert all(isinstance(sentence, str) for sentence in data["result"])


def test_invalid_query():
    response = client.post(
        "/question/", json={"text": "asldkjasldjasldjasdljas"})
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert isinstance(data["detail"], str)


def test_empty_query():
    response = client.post("/question/", json={"text": ""})
    # Depends on validation handling
    assert response.status_code == 422 or response.status_code == 404
