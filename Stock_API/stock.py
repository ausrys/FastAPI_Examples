import yfinance as yf
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Define a Pydantic model to validate the payload


class StockRequest(BaseModel):
    stock_name: str
    period: str


class StockVolumeRequest(BaseModel):
    stock_name: str
    period: str


class StockAvgRequest(BaseModel):
    stock_name: str
    period: str


def fetch_stock_price(stock_name: str, period: str):
    stock = yf.Ticker(stock_name)
    data = stock.history(period=period)

    if data.empty:
        return None

    return data['Close']


def fetch_stock_volume(stock_name: str, period: str):
    stock = yf.Ticker(stock_name)
    data = stock.history(period=period)

    if data.empty:
        return None

    return list(data['Volume'])


@app.post("/get_stock_price")
async def get_stock_price(request: StockRequest):
    stock_name = request.stock_name.upper()
    stock_period = request.period.lower()
    # Fetch stock data using yfinance
    price = fetch_stock_price(stock_name, stock_period)

    if price is None:
        return {"error": "Stock not found"}

    return {"stock_price": list(price)}

# Route to get stock volume


@app.post("/get_stock_volume")
async def get_stock_volume(request: StockVolumeRequest):
    stock_name = request.stock_name.upper()
    stock_period = request.period.lower()
    volume = fetch_stock_volume(stock_name, stock_period)
    if volume is None:
        return {"error": "Stock not found"}
    return {stock_name + " volume:": volume}

# Route to get stock average (moving average)


@app.post("/get_stock_avg")
async def get_stock_avg(request: StockAvgRequest):
    stock_name = request.stock_name.upper()
    period = request.period.lower()

    # Fetch stock data using yfinance
    data = fetch_stock_price(stock_name, period)

    if data is None:
        return {"error": "Stock not found"}

    # Calculate moving average using pandas and numpy
    avg_price = data.mean()
    return {stock_name: avg_price}
