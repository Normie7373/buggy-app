def safe_division(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return dividend / divisor

x = safe_division(1, 1)  # This will work fine
try:
    x = safe_division(1, 0)  # This will raise a ValueError
except ValueError as e:
    print(e)