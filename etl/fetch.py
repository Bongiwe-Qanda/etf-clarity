import yfinance as yf
import pandas as pd

def fetch_etf_data(ticker):
    
    #ticker object
    etf = yf.Ticker(ticker)

    #get historical price data
    data = etf.history(period = "5y")

    data.to_csv(f"data/raw/{ticker}.csv")

    print(f"Fetched data for {ticker} saved to data/raw/{ticker}.csv")

    return data


def fetch_multiple_etf_data(tickers):

    tickers_list = []

    for ticker in tickers:
        tickers_list.append(fetch_etf_data(ticker))
    return tickers_list


if __name__ == "__main__":
    tickers = ["STX40.JO", "SYG4IR.JO", "STXNDQ.JO"]
    fetch_multiple_etf_data(tickers)

