# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from db_singleton import DatabaseSingleton

from api.routes import router

app = FastAPI()
app.include_router(router)

# Create table if not exists
db = DatabaseSingleton("requests.db")
cursor = db.get_cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS requests (
    time INTEGER,
    stock TEXT,
    price FLOAT,
    av_7 FLOAT,
    av_14 FLOAT,
    av_21 FLOAT,
    daily_price FLOAT,
    month_price FLOAT
)""")


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request,
                                        exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Route does not exist, check README file\
                    https://github.com/ausrys/FastAPI_Examples/\
                    tree/main/Stock_API"},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
