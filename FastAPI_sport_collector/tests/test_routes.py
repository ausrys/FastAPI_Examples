from fastapi.testclient import TestClient
from FastAPI_sport_collector.main import app

client = TestClient(app)


def test_news_route():
    response = client.get("/news")
    assert response.status_code == 200
    assert "message" in response.json()


def test_events_route():
    response = client.get("/events")
    assert response.status_code == 200
    assert "message" in response.json()
