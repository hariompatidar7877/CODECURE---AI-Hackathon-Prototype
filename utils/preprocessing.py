import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def filter_country(df, country):
    return df[df['Country'] == country].copy()


def handle_missing(df):
    return df.fillna(method="ffill")
