import pandas as pd
from datetime import datetime
import strategy
import indicators

class Analyzer:
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.strategy = strategy.Strategy()
        self.ticker = ticker
        self.original_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")

        self.max_margin = max(
            self.strategy.rsi_interval,
            self.strategy.sma_interval,
            self.strategy.atr_interval
        )

        data = pd.read_csv("market_data.csv", parse_dates=["Date"])
        data = data[data["Symbol"] == self.ticker].sort_values("Date").reset_index(drop=True)

        idx = data[data["Date"] == self.original_start_date].index

        if len(idx) == 0 or idx[0] < self.max_margin:
            raise ValueError("Invalid start date or insufficient margin.")

        start_idx = idx[0] - self.max_margin
        end_idx = data[data["Date"] <= self.end_date].index.max()

        self.data = data.loc[start_idx:end_idx].reset_index(drop=True)

    def gen_signal(self):
        sma_idx = self.max_margin - self.strategy.sma_interval
        rsi_idx = self.max_margin - self.strategy.rsi_interval
        atr_idx = self.max_margin - self.strategy.atr_interval

        print(sma_idx, rsi_idx, atr_idx)

        sma = indicators.compute_sma(self.data.loc[sma_idx:], self.strategy.sma_interval)
        rsi = indicators.compute_rsi(self.data.loc[rsi_idx:], self.strategy.rsi_interval)

        print(len(sma), len(rsi))
        print(rsi)

if __name__ == '__main__':
    a = Analyzer('AAPL', '2024-06-03', '2024-12-12')
    print(a.gen_signal())