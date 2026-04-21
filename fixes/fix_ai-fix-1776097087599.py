
# app/utils/calculator.py

def add_values(a, b):
    """
    Adds two values together.

    Args:
        a (int or float): The first value to add.
        b (int or float): The second value to add.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If a or b cannot be converted to a number.
    """
    try:
        # Attempt to convert inputs to floats
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        # If inputs cannot be converted to numbers, raise a TypeError
        raise TypeError("Both inputs must be numbers")
