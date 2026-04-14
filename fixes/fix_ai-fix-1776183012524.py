def safe_division(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return dividend / divisor

try:
    x = safe_division(1, 0)
    print(x)
except ValueError as e:
    print(e)