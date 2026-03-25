def add_features(df):
    df['daily_cases'] = df['Cases'].diff().fillna(0)
    df['growth_rate'] = df['daily_cases'].pct_change().fillna(0)
    df['rolling_avg'] = df['daily_cases'].rolling(7).mean().fillna(0)
    return df
