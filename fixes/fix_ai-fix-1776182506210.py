def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(1, 0)
    print(result)
except ValueError as e:
    print(e)