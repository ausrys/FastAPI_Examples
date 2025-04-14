# services/stock_service.py
from datetime import datetime


import yfinance as yf
from db_singleton import DatabaseSingleton

db = DatabaseSingleton("requests.db")
cursor = db.get_cursor()


def fetch_stock(stock_name: str):
    stock = yf.Ticker(stock_name)
    return stock


def save_data(name: str):
    stock = yf.Ticker(name)
    av_7 = stock.history(period="7d")['Close'].mean()
    av_14 = stock.history(period="14d")['Close'].mean()
    av_21 = stock.history(period="21d")['Close'].mean()
    month_price = stock.history(period="1mo")['Close'].mean()
    price = stock.info['regularMarketPrice']
    daily_price = stock.info['previousClose']
    now = datetime.now()
    unix_timestamp = int(now.timestamp())

    cursor.execute("""
            INSERT INTO requests (time, stock, price, av_7, av_14, av_21,\
                month_price, daily_price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (unix_timestamp, name, price, av_7, av_14, av_21,
              month_price, daily_price))
    db.commit()


def get_all_records():
    cursor.execute("SELECT * FROM requests")
    return cursor.fetchall()


def get_records_by_time(timestamp: int):
    cursor.execute("SELECT * FROM requests WHERE time = ?", (timestamp,))
    return cursor.fetchall()
