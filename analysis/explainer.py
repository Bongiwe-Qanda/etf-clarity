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
    print(f"Current price of {ticker}: R{latest_close:.2f}")
    return latest_close
if __name__ == "__main__":
    df = fetch_clean_data("STX40.JO")
    explained = explain_etf("STX40.JO")
    print(explained)