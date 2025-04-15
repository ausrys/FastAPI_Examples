# services/stock_service.py
from datetime import datetime

from db_singleton import DatabaseSingleton
from exceptions import AppException
from utils.yfinance_facade import FinanceFacade

db = DatabaseSingleton("requests.db")
cursor = db.get_cursor()


def save_data(name: str):
    stock = FinanceFacade(name.upper())
    av_7 = stock.get_av_price(period="7d")
    av_14 = stock.get_av_price(period="14d")
    av_21 = stock.get_av_price(period="21d")
    month_price = stock.get_av_price(period="1mo")
    price = stock.get_stock_info('regularMarketPrice')
    daily_price = stock.get_stock_info('previousClose')
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
    rows = cursor.fetchall()
    if not rows:
        raise AppException(
            status_code=404,
            description="No rows found for the provided timestamp.",
            solve="Make sure you're passing a valid UNIX timestamp."
        )
    return rows
