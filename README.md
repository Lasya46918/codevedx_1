# Project 1 — Utility Usage Prediction Tool

## Objective
Store utility usage records in CSV, train a regression model, and estimate electricity usage (kWh) from month and temperature.

## Features
- Menu-driven console interface.
- Add and view usage data.
- CSV file handling.
- Train and save a Random Forest regression model.
- Predict usage from month and temperature.
- Input validation and error handling.

## Run
From this folder:
```bash
pip install -r ../requirements.txt
python main.py
```
Choose **Train model** before prediction. The provided CSV is sample educational data, not a real utility dataset.

## Files
- `main.py`: menu and input validation.
- `data_manager.py`: CSV reading/writing.
- `model.py`: training and prediction.
- `utility_data.csv`: sample records.
