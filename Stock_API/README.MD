# 📈 FastAPI Stock Info Service

This is a simple FastAPI-based API for fetching stock data using the [Yahoo Finance API](https://pypi.org/project/yfinance/). It provides endpoints to retrieve:

- Daily closing prices
- Daily volume data
- Average closing price over a given period

The app uses the `yfinance` package to retrieve data and `FastAPI` for the web framework.

---

## 🚀 Features

- Get closing prices for a stock over a time period
- Get daily volume for a stock over a time period
- Get the average (mean) closing price over a time period
- Input validation using Pydantic
- JSON-based RESTful API

## 📦 Installation


### With out docker:

- Clone the repository
- Inside the stocl_api folder run:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
- Install dependencies
```
pip install -r requirements.txt
```
Run the program in dev:
```
fastapi dev stock.py
```
or 
uvicorn main:stock --reload


### With docker:

```
docker build -t stock-api .
docker run stock-api
```

⏳ Supported Periods
The period field supports any duration valid in the Yahoo Finance history method. Examples include:

1d, 5d, 1mo, 3mo

6mo, 1y, 2y, 5y, 10y

ytd (year-to-date), max


## API ENDPOINTS

1. /get_stock_price
Description: Get daily closing prices for a stock over a specified period.

Method: POST

Payload:
```
{
  "stock_name": "AAPL",
  "period": "5d"
}
```
Response:
```
{
  "stock_price": [
    171.64999389648438,
    172.6199951171875,
    174.99000549316406,
    175.05999755859375,
    175.1199951171875
  ]
}
```

2. /get_stock_volume
Description: Get daily trading volume for a stock over a specified period.

Method: POST

Payload:
```
{
  "stock_name": "MSFT",
  "period": "1mo"
}
```
Response:
```
{
  "MSFT volume:": [
    27490300,
    20314400,
    20161800,
    ...
  ]
}
```

3. /get_stock_avg
Description: Get the average (mean) closing price over the specified period.

Method: POST

Payload:
```
{
  "stock_name": "GOOG",
  "period": "7d"
}
```
Response:
```
{
  "GOOG": 146.25
}
```

## ⏳ Supported Periods
The period field supports any duration valid in the Yahoo Finance history method. Examples include:

1d, 5d, 1mo, 3mo

6mo, 1y, 2y, 5y, 10y

ytd (year-to-date), max