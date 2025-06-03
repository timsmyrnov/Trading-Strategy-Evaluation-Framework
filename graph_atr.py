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

atr = [2.67, 2.64, 2.63, 2.61, 2.62, 2.8, 3.6, 4.29, 4.35, 4.31, 4.46, 4.54, 4.6, 4.61, 4.72, 4.61, 4.69, 4.6, 4.68, 4.84, 4.87, 4.7, 4.71, 4.7, 4.58, 4.57, 4.76, 4.78, 4.91, 4.84, 5.08, 5.3, 5.17, 5.13, 5.07, 5.27, 5.34, 5.21, 5.09, 5.03, 5.03, 5.2, 5.39, 6.7, 6.86, 6.89, 6.78, 6.64, 6.44, 6.29, 6.08, 5.9, 5.7, 5.51, 5.24, 5.07, 5.02, 4.94, 4.83, 4.77, 4.73, 4.85, 4.71, 4.93, 4.95, 4.93, 4.97, 4.94, 4.92, 4.94, 4.85, 4.66, 4.94, 4.76, 4.84, 5.14, 5.16, 5.05, 4.95, 4.83, 4.7, 4.52, 4.57, 4.9, 4.86, 4.76, 4.7, 4.75, 4.72, 4.73, 4.56, 4.38, 4.36, 4.49, 4.46, 4.38, 4.35, 4.21, 4.19, 4.47, 4.32, 4.27, 4.2, 4.04, 4.04, 4.09, 4.2, 4.13, 4.03, 4.09, 4.17, 4.03, 4.13, 3.99, 3.98, 3.97, 3.97, 4.02, 3.98, 3.98, 4.01, 3.91, 3.88, 3.79, 3.65, 3.66, 3.66, 3.67, 3.61, 3.52, 3.45, 3.6, 3.55, 3.62, 3.58]

atr_start_index = len(dates) - len(atr)
atr_dates = dates[atr_start_index:]

fig, ax1 = plt.subplots(figsize=(14, 6))

ax1.plot(dates, close_prices, label="AAPL Close Price", color='black', linewidth=1.5)
ax1.set_xlabel("Date")
ax1.set_ylabel("Close Price", color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(atr_dates, atr, label="14-day ATR", color='purple', linewidth=2.5)
ax2.fill_between(atr_dates, atr, color='purple', alpha=0.2)
ax2.set_ylabel("ATR", color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

plt.title("AAPL Close Price and 14-Day ATR")
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.xticks(rotation=45)
plt.show()