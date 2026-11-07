from data_manager import add_record, show_records
from model import train_model, predict_usage

def get_float(prompt, low=None, high=None):
    value = float(input(prompt))
    if low is not None and value < low:
        raise ValueError(f"Value must be at least {low}.")
    if high is not None and value > high:
        raise ValueError(f"Value must be at most {high}.")
    return value

def main():
    while True:
        print("\nUTILITY USAGE PREDICTION")
        print("1. Add usage record")
        print("2. View records")
        print("3. Train model")
        print("4. Predict usage")
        print("5. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                month = int(get_float("Month (1-12): ", 1, 12))
                temperature = get_float("Temperature in °C: ", -50, 60)
                usage = get_float("Usage in kWh: ", 0)
                add_record(month, temperature, usage)
                print("Record saved.")
            elif choice == "2":
                show_records()
            elif choice == "3":
                train_model()
            elif choice == "4":
                month = int(get_float("Month (1-12): ", 1, 12))
                temperature = get_float("Temperature in °C: ", -50, 60)
                result = predict_usage(month, temperature)
                print(f"Estimated usage: {result:.2f} kWh")
                print("Educational estimate only; not a billing forecast.")
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Choose a number from 1 to 5.")
        except (ValueError, OSError, FileNotFoundError) as exc:
            print("Error:", exc)

if __name__ == "__main__":
    main()
