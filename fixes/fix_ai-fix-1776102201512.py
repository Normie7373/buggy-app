
def add_values(a, b):
    """
    Adds two values together.

    Args:
        a (int or float or str): The first value to add.
        b (int or float or str): The second value to add.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If either a or b cannot be converted to a number.
    """
    try:
        # Attempt to convert inputs to floats
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        # If conversion fails, raise a TypeError with a helpful message
        raise TypeError("Both inputs must be numbers or strings that can be converted to numbers")
