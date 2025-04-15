from fastapi.testclient import TestClient
from stock import app

client = TestClient(app)


def test_get_stock_price():
    response = client.post(
        "/get_stock_price", json={"stock_name": "msft", "period": "7d"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['stock_price'], list)
    assert len(data['stock_price']) == 7
    assert all(isinstance(item, float) for item in data['stock_price'])
    response = client.post(
        "/get_stock_price", json={"stock_name": "msft", "period": "ad"})
    assert response.status_code == 400
    assert "description" in response.json()
    assert "solve" in response.json()


def test_get_stock_volume():
    response = client.post(
        "/get_stock_volume", json={"stock_name": "msft", "period": "7d"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['MSFT volume'], list)
    assert len(data['MSFT volume']) == 7
    response = client.post(
        "/get_stock_volume", json={"stock_name": "msft", "period": "d"})
    assert response.status_code == 400
    assert "description" in response.json()
    assert "solve" in response.json()


def test_get_full_table():
    response = client.get("/get_full_table")
    data = response.json()
    assert 'table_contents' in data


def test_check_db_time():
    response = client.get("/check_db_time?time=1744375052")
    data = response.json()
    assert 'time_records' in data
    assert isinstance(data['time_records'], list)
    assert len(data['time_records'][0]) == 8
    response = client.get("/check_db_time?time=1")
    assert response.status_code == 404
    assert "description" in response.json()
    assert "solve" in response.json()


def test_stock_avg():
    response = client.post(
        "/get_stock_avg", json={"stock_name": "msft", "period": "7d"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['MSFT'], float)
    response = client.post(
        "/get_stock_avg", json={"stock_name": "msft", "period": "d"})
    assert response.status_code == 400
    assert "description" in response.json()
    assert "solve" in response.json()


def test_get_any_route():
    response = client.get("/")
    assert response.status_code == 404
    assert "description" in response.json()
    assert "solve" in response.json()
