import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from etl.transform import transform_raw_data
from etl.fetch import fetch_etf_data
from db import get_connection
import pandas as pd

def load_etf_data(df,ticker):
    connection = get_connection()

    cursor = connection.cursor()

    for index, row in df.iterrows():
        cursor.execute("""
    INSERT INTO etf_prices (ticker, date, open, high, low, close, volume, dividends)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", (ticker, row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Dividends']))
        
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Loaded {len(df)} rows for {ticker}")   
            
if __name__ == "__main__":
    ticker = "STX40.JO"
    raw = fetch_etf_data(ticker)
    clean = transform_raw_data(raw)
    load_etf_data(clean, ticker)