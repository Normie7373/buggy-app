def buggy_function():
    a = 5
    b = "10"
    try:
        b = int(b)  # convert string to integer
        return a + b
    except ValueError:
        return "Error: Cannot convert string to integer"

print(buggy_function())