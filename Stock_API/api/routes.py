# api/routes.py

from fastapi import APIRouter
from models.schemas import StockRequest, StockVolumeRequest, StockAvgRequest
from services.stock_service import fetch_stock_data, save_data, \
    get_all_records, get_records_by_time

from exceptions import AppException

router = APIRouter()


@router.post("/get_stock_price")
async def get_stock_price(request: StockRequest):
    try:
        data = fetch_stock_data(
            request.stock_name.upper(), request.period.lower())
    except Exception:
        return AppException(description="Provided stock name or period was \
            incorrect",
                            solve="Check if values are correct",
                            status_code=400
                            )
    save_data(request.stock_name.upper())
    return {"stock_price": list(data['Close'])}


@router.post("/get_stock_volume")
async def get_stock_volume(request: StockVolumeRequest):
    try:
        data = fetch_stock_data(
            request.stock_name.upper(), request.period.lower())
        save_data(request.stock_name.upper())
        return {request.stock_name.upper() + " volume": list(data['Volume'])}
    except Exception:
        return AppException(description="Provided stock name or period was \
            incorrect",
                            solve="Check if values are correct",
                            status_code=400
                            )


@router.post("/get_stock_avg")
async def get_stock_avg(request: StockAvgRequest):
    try:
        data = fetch_stock_data(
            request.stock_name.upper(), request.period.lower())
        save_data(request.stock_name.upper())
        avg_price = data['Close'].mean()
        return {request.stock_name.upper(): avg_price}
    except Exception:
        return AppException(description="Provided stock name or period was \
            incorrect",
                            solve="Check if values are correct",
                            status_code=400
                            )


@router.get("/get_full_table")
async def get_full_table():
    return {"table_contents": get_all_records()}


@router.get("/check_db_time")
async def check_db_time(time: int):
    rows = get_records_by_time(time)
    if not rows:
        return AppException(
            status_code=404,
            description="No rows found for the provided timestamp.",
            solve="Make sure you're passing a valid UNIX timestamp."
        )
    return {"time_records": rows}
