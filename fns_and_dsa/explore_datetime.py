from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days_to_add):
    """Calculate and display the future date after adding a given number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} day(s): {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    while True:
        try:
            days = int(input("Enter number of days to add: "))
            calculate_future_date(days)
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
