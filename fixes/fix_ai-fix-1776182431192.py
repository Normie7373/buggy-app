def divide(num, denom):
    if denom == 0:
        return "Error: Division by zero is not allowed"
    else:
        return num / denom

x = divide(1, 0)
print(x)