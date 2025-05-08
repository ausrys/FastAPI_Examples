# api/routes.py

from fastapi import APIRouter
from models.schemas import StockRequest, StockVolumeRequest, StockAvgRequest
from services.stock_service import save_data, \
    get_all_records, get_records_by_time
from utils.yfinance_facade import FinanceFacade

router = APIRouter()


@router.post("/get_stock_price")
async def get_stock_price(request: StockRequest):
    stock = FinanceFacade(request.stock_name)
    save_data(request.stock_name)
    return {"stock_price": stock.get_period_prices(request.period)}


@router.post("/get_stock_volume")
async def get_stock_volume(request: StockVolumeRequest):
    stock = FinanceFacade(request.stock_name)
    save_data(request.stock_name)

    return {request.stock_name.upper() + " volume":
            stock.get_period_volumes(request.period)}


@router.post("/get_stock_avg")
async def get_stock_avg(request: StockAvgRequest):
    stock = FinanceFacade(request.stock_name)
    save_data(request.stock_name)
    avg_price = stock.get_av_price(request.period)
    return {request.stock_name.upper(): avg_price}


@router.get("/get_full_table")
async def get_full_table():
    return {"table_contents": get_all_records()}


@router.get("/check_db_time")
async def check_db_time(time: int):
    rows = get_records_by_time(time)
    return {"time_records": rows}


@router.get("/get_msft_api")
async def get_msft_api():
    stock = FinanceFacade('msft')
    msft_current = stock.get_stock_info('regularMarketPrice')
    return {"name": "msft", "msft_stock_price_current": msft_current}
