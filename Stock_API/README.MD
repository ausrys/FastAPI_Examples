# 📈 FastAPI Stock Info Service

This is a simple FastAPI-based API for fetching stock data using the [Yahoo Finance API](https://pypi.org/project/yfinance/). It provides endpoints to retrieve:

- Daily closing prices
- Daily volume data
- Average closing price over a given period

The app uses the `yfinance` package to retrieve data and `FastAPI` for the web framework.

---
## [Confluence page](https://orioninc-team-kyh3w470.atlassian.net/wiki/spaces/~712020da8e289c17a1423fa042ec5ea224cc6a/pages/131260/Stock+FASTAPI)
---


---
## [SolarCloud](https://sonarcloud.io/project/overview?id=ausrys_FastAPI_Examples)
---

## 🚀 Features

- Get closing prices for a stock over a time period
- Get daily volume for a stock over a time period
- Get the average (mean) closing price over a time period
- Input validation using Pydantic
- JSON-based RESTful API
- Saves a stock info to the database for later use
- Ability to find records based on time

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

4. /get_full_table

Description: Get all the records in the requests table.

Method: GET

5. /check_db_time

Description: Get the records where time is the same as provided.

Method: GET

Payload:
```
{
  "time": 1744365204,
}
```
Response:
```
{
  "time_records": [
    [
      1744365204,
      "MSFT",
      381.35,
      371.33571079799106,
      378.89428274972096,
      381.42809331984745,
      381.4656504755435,
      390.49
    ]
  ]
}
```

## Record information

Every stock is saved in the database on each API request.
Information of the stock: time, stock, price, av_7, av_14, av_21, month_price, daily_price
- time -> the time a the record creation
- stock -> stock name
- price -> current price
- av_*, month_price -> avarage price based on the interval
- daily_price -> last closed price


## ⏳ Supported Periods

The period field supports any duration valid in the Yahoo Finance history method. Examples include:

1d, 5d, 1mo, 3mo

6mo, 1y, 2y, 5y, 10y

ytd (year-to-date), max