def buggy_function():
    a = 5
    b = "10"
    return a + int(b)  # convert string to integer

print(buggy_function())  # print the result