# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            temp_input = input("Enter the temperature (e.g., 100): ").strip()
            temp = float(temp_input)
            
            unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
            
            if unit == 'C':
                converted = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted:.2f}°F")
                break
            elif unit == 'F':
                converted = convert_to_celsius(temp)
                print(f"{temp}°F is {converted:.2f}°C")
                break
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
