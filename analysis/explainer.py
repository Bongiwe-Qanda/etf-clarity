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

if __name__ == "__main__":
    df = fetch_clean_data("STX40.JO")
    print(df.head())