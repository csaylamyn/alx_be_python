# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.
    
    Args:
        numerator: The numerator (can be string input).
        denominator: The denominator (can be string input).
        
    Returns:
        Result of division or error message string.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
