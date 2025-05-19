import get_market_data as gmd
import pandas as pd

def compute_sma(data: pd.DataFrame, period: int) -> list:
    df = data

    # Compute initial sum based on window size (period)
    price_sum = sum(df['Close'].iloc[:period])

    sma_list = [round(price_sum / period, 2)]

    for i in range(period, len(df)):
        u_bound = df['Close'].iloc[i]
        l_bound = df['Close'].iloc[i - period]

        price_sum = price_sum + u_bound - l_bound
        sma_list.append(round(float(price_sum / period), 2))

    return sma_list