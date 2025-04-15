import yfinance as yf

from exceptions import AppException


class FinanceFacade:
    def __init__(self, stock_name: str) -> None:
        self.stock_name = stock_name.upper()
        self.ticker = yf.Ticker(stock_name)
        try:
            self.ticker.info
        except AttributeError as exc:
            raise AppException(description='''Provided stock name was\
                incorrect''',
                               solve="Check if values are correct",
                               status_code=400
                               ) from exc

    def __get_history_data(self, period):
        data = self.ticker.history(period=period)
        if len(data) == 0:
            raise AppException(
                status_code=400, description='''Provided period was incorrect
                or there was no data''', solve="Check parameters")

        return data

    def get_av_price(self, period):
        hist_data = self.__get_history_data(period)
        av = hist_data['Close'].mean()
        return av

    def get_period_prices(self, period):
        hist_data = self.__get_history_data(period)
        return list(hist_data['Cloe'])

    def get_period_volumes(self, period):
        hist_data = self.__get_history_data(period)
        return list(hist_data['Volume'])

    def get_stock_info(self, attribute):
        return self.ticker.info[attribute]
