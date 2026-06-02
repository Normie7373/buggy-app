def buggy_function():
    a = 5
    b = "10"
    try:
        b = int(b)
        return a + b
    except ValueError:
        return "Error: Cannot convert 'b' to an integer"

print(buggy_function())