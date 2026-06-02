def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

x = divide(1, 1)  # This will work fine
try:
    y = divide(1, 0)  # This will raise an error
except ValueError as e:
    print(e)