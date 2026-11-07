from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).with_name("utility_data.csv")
COLUMNS = ["month", "temperature_c", "usage_kwh"]

def load_data():
    if not DATA_FILE.exists():
        pd.DataFrame(columns=COLUMNS).to_csv(DATA_FILE, index=False)
    return pd.read_csv(DATA_FILE)

def add_record(month, temperature_c, usage_kwh):
    data = load_data()
    new_row = pd.DataFrame([{
        "month": month, "temperature_c": temperature_c,
        "usage_kwh": usage_kwh
    }])
    pd.concat([data, new_row], ignore_index=True).to_csv(DATA_FILE, index=False)

def show_records():
    data = load_data()
    if data.empty:
        print("No records yet.")
    else:
        print(data.to_string(index=False))
