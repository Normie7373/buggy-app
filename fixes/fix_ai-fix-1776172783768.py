def buggy_function():
    a = 5
    b = "10"
    return a + int(b)  # Convert string to integer before adding

print(buggy_function())  # Added print statement to see the result