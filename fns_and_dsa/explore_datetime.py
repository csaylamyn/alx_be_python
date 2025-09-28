from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days_to_add):
    """Calculate and display the future date after adding a specified number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    while True:
        try:
            days_input = input("Enter the number of days to add to the current date: ").strip()
            days = int(days_input)
            calculate_future_date(days)
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
