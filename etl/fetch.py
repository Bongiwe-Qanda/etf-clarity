import yfinance as yf
import pandas as pd

def fetch_etf_data(ticker):
    
    #ticker object
    etf = yf.Ticker(ticker)

    #get historical price data
    data = etf.history(period = "5y")

    data.to_csv(f"data/raw/{ticker}.csv")

    return data

    print(f"Fetched data for {ticker} saved to data/raw/{ticker}.csv")

if __name__ == "__main__":
    fetch_etf_data("STX40.JO")