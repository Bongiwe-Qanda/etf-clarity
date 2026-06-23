import pandas as pd


def handle_missing_data(df):
    df = df.dropna()
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def convert_data_format(df):
    df = df.reset_index()
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def drop_stock_splits(df):
    df = df.drop('Stock Splits',axis = 1, errors = 'ignore')
    return df

def transform_raw_data(df):
    no_stock_split = drop_stock_splits(df)
    no_empty_cells = handle_missing_data(no_stock_split)
    no_duplicates = remove_duplicates(no_empty_cells)
    no_incorrect_date = convert_data_format(no_duplicates)

    return no_incorrect_date


if __name__ == "__main__":
    from fetch import fetch_etf_data
    raw_data = fetch_etf_data("STX40.JO")
    clean_data = transform_raw_data(raw_data)
    print(clean_data.head(10))
