class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Create an instance of the Calculator class
calc = Calculator()

try:
    # Attempt to divide 5 by 0
    result = calc.divide(5, 0)
except ValueError as e:
    # Handle the ValueError if division by zero occurs
    print(f"Error: {e}")