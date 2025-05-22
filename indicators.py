import get_market_data as gmd
import pandas as pd

def compute_sma(data: pd.DataFrame, interval: int) -> list:
    
    # Compute initial sum based on window size (period)
    price_sum = sum(data['Close'].iloc[:interval])

    sma_list = []

    for i in range(interval, len(data)):
        sma_list.append(round(float(price_sum / interval), 2))

        u_bound = data['Close'].iloc[i]
        l_bound = data['Close'].iloc[i - interval]

        price_sum = price_sum + u_bound - l_bound

    return sma_list

def compute_rsi(data: pd.DataFrame, interval: int) -> list:
    gain_pct = []
    loss_pct = []

    for i in range(1, interval + 1):
        pct_change = float((data['Close'].iloc[i] - data['Close'].iloc[i-1]) / data['Close'].iloc[i-1] * 100)

        gain_pct.append(pct_change if pct_change > 0 else 0)
        loss_pct.append(abs(pct_change) if pct_change < 0 else 0)

    rsi_list = [100] if sum(loss_pct) == 0 else [round(100 - 100 / (1 + (sum(gain_pct) / interval) / (sum(loss_pct) / interval)), 2)]

    for j in range(interval + 1, len(data) - 1):
        rsi_list.append(j)

    return len(rsi_list)