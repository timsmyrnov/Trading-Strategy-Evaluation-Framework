import get_market_data as gmd
import pandas as pd

def compute_sma(data: pd.DataFrame, period: int) -> list:
    # Compute initial sum based on window size (period)
    price_sum = sum(data['Close'].iloc[:period])

    sma_list = []

    for i in range(period, len(data)):
        sma_list.append(round(float(price_sum / period), 2))

        u_bound = data['Close'].iloc[i]
        l_bound = data['Close'].iloc[i - period]

        price_sum = price_sum + u_bound - l_bound

    return sma_list

def compute_rsi(data: pd.DataFrame, period: int) -> list:
    ...