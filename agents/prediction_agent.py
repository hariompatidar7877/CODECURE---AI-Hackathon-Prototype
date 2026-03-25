import joblib
from config import MODEL_PATH, FORECAST_DAYS

class PredictionAgent:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, df):
        latest = df[['daily_cases', 'rolling_avg']].tail(1)
        prediction = self.model.predict(latest)

        return prediction[0]
