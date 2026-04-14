def divide_numbers(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return dividend / divisor

try:
    result = divide_numbers(10, 0)
    print(result)
except ValueError as e:
    print(f"Error: {e}")