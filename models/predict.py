import joblib
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)

def predict(data):
    return model.predict(data)
