import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

df = pd.read_csv("market_data.csv", parse_dates=["Date"])
mask = (df["Symbol"] == "AAPL") & (df["Date"] >= "2024-06-03") & (df["Date"] <= "2024-12-12")
data = df[mask].to_csv(index=False, header=False)

df = pd.read_csv(StringIO(data), header=None,
                 names=["Date", "Symbol", "Open", "High", "Low", "Close", "Volume"])
df["Date"] = pd.to_datetime(df["Date"])

close_prices = df["Close"].tolist()
dates = df["Date"].tolist()

rsi = [71.0, 71.52, 73.88, 68.31, 72.23, 59.92, 76.38, 79.88, 80.48, 76.82, 79.26, 74.53, 66.2, 62.54, 63.2, 64.17, 68.19, 68.93, 62.49, 68.22, 70.89, 71.81, 74.96, 75.84, 76.36, 78.79, 69.3, 71.39, 73.84, 74.1, 64.49, 57.95, 58.08, 57.56, 58.74, 49.61, 48.26, 48.94, 49.35, 50.24, 55.17, 49.29, 51.57, 38.53, 36.51, 40.77, 45.99, 49.91, 51.87, 56.28, 56.79, 60.1, 61.5, 61.22, 61.93, 61.72, 58.01, 61.14, 61.58, 62.73, 59.28, 63.91, 62.11, 50.12, 47.03, 49.71, 47.11, 47.29, 45.84, 50.97, 51.18, 50.6, 39.56, 40.65, 48.89, 60.91, 59.71, 56.62, 57.84, 55.96, 57.68, 58.09, 65.15, 52.92, 53.74, 51.86, 53.64, 45.51, 51.92, 56.88, 56.06, 53.59, 58.56, 61.52, 57.94, 58.41, 61.94, 63.63, 62.38, 53.11, 52.79, 54.12, 57.17, 57.58, 50.69, 43.95, 39.79, 38.59, 41.63, 40.54, 49.77, 49.31, 44.82, 44.82, 46.55, 52.17, 46.75, 51.87, 52.29, 53.5, 52.55, 54.98, 59.87, 62.99, 62.68, 66.01, 68.78, 72.09, 72.46, 72.49, 71.89, 76.08, 77.02, 73.14, 74.73]

plt.figure(figsize=(12, 6))
plt.plot(dates, close_prices, label="AAPL Close Prices", color='#1f7ea3')
plt.plot(dates, rsi, label="14-day RSI", color='black')
plt.axhline(y=0, color='gray', linestyle='solid')
plt.axhline(y=30, color='purple', linestyle='dashed')
plt.axhline(y=70, color='purple', linestyle='dashed')
plt.axhline(y=100, color='gray', linestyle='solid')

plt.title("AAPL Close Prices vs 14-day RSI")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()