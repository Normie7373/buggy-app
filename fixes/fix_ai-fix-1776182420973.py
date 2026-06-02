def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b

x = divide(1, 0)
print(x)