import joblib
from sklearn.ensemble import RandomForestRegressor
from utils.preprocessing import load_data
from utils.feature_engineering import add_features
from config import DATA_PATH, MODEL_PATH


def train():

    df = load_data(DATA_PATH)
    df = add_features(df)

    X = df[['daily_cases', 'rolling_avg']]
    y = df['Cases']

    model = RandomForestRegressor()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)

    print("Model trained and saved")


if __name__ == "__main__":
    train()
