def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    x = divide(1, 0)
except ValueError as e:
    print(e)