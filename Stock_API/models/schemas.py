from pydantic import BaseModel


class StockRequest(BaseModel):
    stock_name: str
    period: str


class StockVolumeRequest(BaseModel):
    stock_name: str
    period: str


class StockAvgRequest(BaseModel):
    stock_name: str
    period: str
