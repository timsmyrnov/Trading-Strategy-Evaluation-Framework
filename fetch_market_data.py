import yfinance as yf
import pandas as pd

def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()

    data['Symbol'] = ticker
    data = data[['Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume']]

    numerical_columns = ['Open', 'High', 'Low', 'Close']
    data[numerical_columns] = data[numerical_columns].round(2)

    file_name = f'{ticker}_historical_data.csv'
    data.to_csv(file_name, index=False)

    return file_name

if __name__ == '__main__':
    download_data('AAPL', '2022-04-02', '2024-05-03')