import yfinance as yf
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from db_singleton import DatabaseSingleton

db = DatabaseSingleton("requests.db")
cursor = db.get_cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS requests (
                        time DATETIME,
                        stock TEXT,
                        price FLOAT,
                        av_7 FLOAT,
                        av_14 FLOAT,
                        av_21 FLOAT,
                        daily_price FLOAT,
                        month_price FLOAT)''')
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


# class StockDateRecord(BaseModel):
#     time: int


def fetch_stock_data(stock_name: str, period: str):
    stock = yf.Ticker(stock_name)
    data = stock.history(period=period)
    if data.empty:
        return None

    return data


def save_data(name):
    stock = yf.Ticker(name)
    av_7 = stock.history(period="7d")['Close'].mean()
    av_14 = stock.history(period="14d")['Close'].mean()
    av_21 = stock.history(period="21d")['Close'].mean()
    month_price = stock.history(period="1mo")['Close'].mean()
    price = stock.info['regularMarketPrice']
    daily_price = stock.info['previousClose']
    now = datetime.now()
    unix_timestamp = int(now.timestamp())
    cursor.execute(
        "INSERT INTO requests (time, stock, price, av_7, av_14, av_21,\
            month_price, daily_price) VALUES\
                (?, ?, ?, ?, ?, ?, ?, ?)", (unix_timestamp, name, price,
                                            av_7, av_14,
                                            av_21, daily_price,
                                            month_price))
    db.commit()


@app.post("/get_stock_price")
async def get_stock_price(request: StockRequest):
    stock_name = request.stock_name.upper()
    stock_period = request.period.lower()
    # Fetch stock data using yfinance
    data = fetch_stock_data(stock_name, stock_period)

    if data is None:
        return {"error": "Stock not found"}
        # Save to db
    save_data(stock_name)
    return {"stock_price": list(data['Close'])}

# Route to get stock volume


@app.post("/get_stock_volume")
async def get_stock_volume(request: StockVolumeRequest):
    stock_name = request.stock_name.upper()
    stock_period = request.period.lower()
    data = fetch_stock_data(stock_name, stock_period)
    if data is None:
        return {"error": "Stock not found"}
    # Save to db
    save_data(data)

    return {stock_name + " volume:": data['Volume']}

# Route to get stock average (moving average)


@app.post("/get_stock_avg")
async def get_stock_avg(request: StockAvgRequest):
    stock_name = request.stock_name.upper()
    period = request.period.lower()

    # Fetch stock data using yfinance
    data = fetch_stock_data(stock_name, period)

    if data is None:
        return {"error": "Stock not found"}
    # Save to db
    save_data(stock_name)
    # Calculate moving average using pandas and numpy
    avg_price = data['Close'].mean()
    return {stock_name: avg_price}


@app.get("/get_full_table")
async def get_full_table():
    cursor.execute("SELECT * FROM requests")
    rows = cursor.fetchall()
    if rows:
        return {"table_contents": rows}


@app.get("/check_db_time")
async def check_db_time(time):
    cursor.execute("SELECT * FROM requests WHERE time = ?", (time,))
    rows = cursor.fetchall()
    if not rows:
        return {"No rows where found with the provided time stamp"}
    return {"time_records": rows}
