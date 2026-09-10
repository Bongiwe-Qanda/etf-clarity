import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from db import get_connection

def fetch_clean_data(ticker):
    connection = get_connection()

    df = pd.read_sql(
    "SELECT * FROM etf_prices WHERE ticker = %s",
    connection,
    params=(ticker,)
)
    connection.close()
    return df

def explain_etf(ticker):
    clean_data = fetch_clean_data(ticker)
    latest_close = clean_data["close"].iloc[-1]
    

    # price 1 year ago which is approximately 252 rows back
    price_1y_ago = clean_data["close"].iloc[-252]
    return_1y = ((latest_close - price_1y_ago) / price_1y_ago) * 100

    print(f"""
ETF: {ticker}
Current price: R{latest_close:.2f} per unit
1 year return: {return_1y:.2f}%

What this means:
If you had invested R10,000 in {ticker} one year ago, 
it would be worth R{10000 * (1 + return_1y/100):,.2f} today.
""")
    
    
    return {
    "ticker": ticker,
    "current_price": latest_close,
    "return_1y": return_1y
}


if __name__ == "__main__":
    df = fetch_clean_data("STX40.JO")
    explained = explain_etf("STX40.JO")
    print(explained)