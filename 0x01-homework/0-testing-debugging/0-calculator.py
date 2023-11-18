class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

# Create an instance of the Calculator class
calc = Calculator()

# Example calculations
sum_result = calc.add(5, 3)
diff_result = calc.subtract(8, 4)
product_result = calc.multiply(2, 6)

try:
    division_result = calc.divide(10, 2)
    print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {product_result}, Division: {division_result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")