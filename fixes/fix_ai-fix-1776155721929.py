
# calculator.py

def add_numbers(num1, num2):
    """
    Adds two numbers together.

    Args:
    num1 (int or str): The first number.
    num2 (int or str): The second number.

    Returns:
    int: The sum of num1 and num2.
    """
    try:
        # Attempt to convert num1 and num2 to integers
        num1 = int(num1)
        num2 = int(num2)
        # Add the numbers together
        result = num1 + num2
        return result
    except ValueError:
        # If the conversion fails, raise a ValueError
        raise ValueError("Both operands must be numeric")

# Example usage:
print(add_numbers(5, 10))  # Output: 15
print(add_numbers("5", "10"))  # Output: 15
try:
    print(add_numbers("five", 10))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Both operands must be numeric
