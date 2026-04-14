import logging
import json

# Configure logging
logging.basicConfig(level=logging.ERROR)

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        # Log the error details
        logging.error("Error occurred while dividing numbers", exc_info=True)
        error_details = {
            "error_type": type(e).__name__,
            "message": str(e),
            "file": __file__,
            "line": 13,
            "root_cause": "Division by zero",
            "severity": "high"
        }
        return json.dumps(error_details)

# Test the function
print(divide_numbers(10, 0))