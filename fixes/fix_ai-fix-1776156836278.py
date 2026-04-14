
import logging
import json

# Configure logging
logging.basicConfig(level=logging.ERROR)

def handle_error(exception):
    """Handle exceptions and log error details."""
    error_details = {
        "error_type": type(exception).__name__,
        "message": str(exception),
        "file": exception.__traceback__.tb_frame.f_code.co_filename,
        "line": exception.__traceback__.tb_lineno,
        "root_cause": "Unhandled exception",
        "severity": "high"
    }
    logging.error(json.dumps(error_details))
    return error_details

# Example usage
try:
    # Code that might raise an exception
    x = 1 / 0
except Exception as e:
    error_details = handle_error(e)
    print(json.dumps(error_details))
