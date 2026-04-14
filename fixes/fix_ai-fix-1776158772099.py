import logging
import json

# Configure logging
logging.basicConfig(level=logging.ERROR)

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        error_data = {
            "error_type": "ZeroDivisionError",
            "message": str(e),
            "file": __file__,
            "line": 13,
            "root_cause": "Division by zero",
            "severity": "high"
        }
        logging.error(json.dumps(error_data))
        return error_data
    except Exception as e:
        error_data = {
            "error_type": "unknown",
            "message": str(e),
            "file": __file__,
            "line": 19,
            "root_cause": "unknown",
            "severity": "high"
        }
        logging.error(json.dumps(error_data))
        return error_data

# Test the function
print(divide_numbers(10, 0))