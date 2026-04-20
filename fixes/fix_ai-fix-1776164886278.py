import logging
import json

# Configure logging
logging.basicConfig(level=logging.ERROR)

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        # Log the error with detailed information
        logging.error(f"Error: {e}, File: {__file__}, Line: {e.__traceback__.tb_lineno}")
        # Return a detailed error message
        return json.dumps({
            "error_type": "ZeroDivisionError",
            "message": str(e),
            "file": __file__,
            "line": e.__traceback__.tb_lineno,
            "root_cause": "Division by zero",
            "severity": "high"
        })

# Test the function
print(divide_numbers(10, 0))