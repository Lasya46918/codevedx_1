from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "utility_data.csv"
MODEL_FILE = HERE / "utility_model.joblib"
FEATURES = ["month", "temperature_c"]

def train_model():
    data = pd.read_csv(DATA_FILE)
    if len(data) < 5:
        print("Add at least 5 records before training.")
        return False
    if data[FEATURES + ["usage_kwh"]].isnull().any().any():
        print("Dataset contains missing values; correct them before training.")
        return False
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(data[FEATURES], data["usage_kwh"])
    joblib.dump(model, MODEL_FILE)
    print(f"Model saved to {MODEL_FILE.name}. Training rows: {len(data)}")
    return True

def predict_usage(month, temperature_c):
    if not MODEL_FILE.exists():
        raise FileNotFoundError("Model not found. Train the model first.")
    model = joblib.load(MODEL_FILE)
    sample = pd.DataFrame([{"month": month, "temperature_c": temperature_c}])
    return float(model.predict(sample)[0])
