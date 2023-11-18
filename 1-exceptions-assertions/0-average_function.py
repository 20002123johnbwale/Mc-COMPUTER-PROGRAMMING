from 0-calculator import Calculator, DivisionByZeroError

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty.")

    # Create a Calculator instance
    calculator = Calculator()
    
    # Calculate the total and count of numbers
    total = sum(numbers)
    count = len(numbers)

    try:
        # Use the Calculator class to perform division
        average = calculator.divide(total, count)
        return average
    except DivisionByZeroError as e:
        # Handle the custom DivisionByZeroError
        print(f"Error: {e}")
        return None

# Example usage:
numbers = [1, 2, 3, 4, 5]
try:
    # Try to calculate the average and handle exceptions
    result = calculate_average(numbers)
    if result is not None:
        print(f"The average is: {result}")
except ValueError as e:
    # Handle the ValueError (empty list)
    print(f"Error: {e}")
3