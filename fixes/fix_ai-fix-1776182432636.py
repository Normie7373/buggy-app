def safe_division(dividend, divisor):
    if divisor == 0:
        return "Error: Division by zero is not allowed"
    else:
        return dividend / divisor

x = safe_division(1, 0)
print(x)