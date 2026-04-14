
# app/utils/calculator.py

def add_values(a, b):
    """
    Adds two values together.
    
    Args:
        a (int or str): The first value.
        b (int or str): The second value.
    
    Returns:
        int: The sum of a and b.
    
    Raises:
        ValueError: If either a or b cannot be converted to an integer.
    """
    try:
        # Attempt to convert both a and b to integers
        a = int(a)
        b = int(b)
    except ValueError:
        # If either a or b cannot be converted, raise a ValueError
        raise ValueError("Both values must be numeric")
    
    # Now that we're sure both a and b are integers, we can safely add them
    return a + b
