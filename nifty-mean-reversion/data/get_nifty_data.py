import yfinance as yf
import pandas as pd

def download_nifty_data(start="2015-01-01", end="2024-12-31"):
    ticker = "^NSEI"  # Nifty 50 Index on Yahoo Finance
    data = yf.download(ticker, start=start, end=end)
    data.to_csv("nifty_daily_data.csv")
    print(f"✅ Downloaded Nifty 50 data from {start} to {end} → saved as 'nifty_daily_data.csv'")

if __name__ == "__main__":
    download_nifty_data()
