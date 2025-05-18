import strategy
import fetch_market_data as fmd
import indicators
from datetime import datetime, timedelta

class Analyzer:
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.strategy = strategy.Strategy()

        # Consider the preceding k - 1 days for proper indicator computation
        margin = max(self.strategy.rsi_period, self.strategy.sma_period, self.strategy.atr_period) - 1

        self.start_date = (datetime.strptime(start_date, "%Y-%m-%d") - timedelta(days=margin)).strftime("%Y-%m-%d")
        self.end_date = end_date

        self.data_file = fmd.download_data(ticker, self.start_date, self.end_date)

    def gen_signal(self):
        rsi = indicators.compute_rsi()
        sma = indicators.compute_sma()
        atr = indicators.compute_atr()

a = Analyzer('AAPL', '2024-05-03', '2024-05-28')
print(a.start_date, a.end_date)