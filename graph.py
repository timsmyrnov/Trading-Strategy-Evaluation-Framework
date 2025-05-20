import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

aapl_data = """
2024-05-03,AAPL,185.53,185.88,181.56,182.28,163224100.0
2024-05-06,AAPL,181.26,183.09,179.34,180.62,78569700.0
2024-05-07,AAPL,182.35,183.79,180.23,181.31,77305800.0
2024-05-08,AAPL,181.75,181.97,180.36,181.64,45057100.0
2024-05-09,AAPL,181.46,183.55,181.02,183.46,48983000.0
2024-05-10,AAPL,184.04,184.23,181.28,182.2,50759500.0
2024-05-13,AAPL,184.58,186.23,183.76,185.41,72044800.0
2024-05-14,AAPL,186.64,187.42,185.42,186.56,52393600.0
2024-05-15,AAPL,187.04,189.76,186.5,188.84,70400000.0
2024-05-16,AAPL,189.58,190.21,188.78,188.96,52845200.0
2024-05-17,AAPL,188.63,189.92,188.3,188.99,41282900.0
2024-05-20,AAPL,188.45,191.03,188.13,190.15,44361300.0
2024-05-21,AAPL,190.2,191.83,190.03,191.45,42309400.0
2024-05-22,AAPL,191.38,191.92,189.38,190.01,34648500.0
2024-05-23,AAPL,190.09,190.11,185.76,186.01,51005900.0
2024-05-24,AAPL,187.94,189.69,187.16,189.1,36294600.0
2024-05-28,AAPL,190.62,192.1,188.22,189.11,52280100.0
"""

df = pd.read_csv(StringIO(aapl_data), header=None,
                 names=["Date", "Symbol", "Open", "High", "Low", "Close", "Volume"])
df["Date"] = pd.to_datetime(df["Date"])

close_prices = df["Close"].tolist()
dates = df["Date"].tolist()

custom_sma = [
    171.37, 171.35, 171.34, 171.36, 171.36, 171.43, 171.48, 171.61, 171.86,
    172.26, 172.68, 173.1, 173.5, 173.9, 174.26, 174.57, 174.92
]

plt.figure(figsize=(12, 6))
plt.plot(dates, close_prices, label="AAPL Close Prices", marker='o')
plt.plot(dates, custom_sma, label="Custom SMA", marker='x')

plt.title("AAPL Close Prices vs Custom SMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()