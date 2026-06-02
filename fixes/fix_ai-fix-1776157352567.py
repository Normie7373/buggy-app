import logging
import traceback

def handle_exception(exc):
    error_message = f"An error occurred: {str(exc)}"
    logging.error(error_message)
    logging.error(traceback.format_exc())
    return {
        "error_type": type(exc).__name__,
        "message": str(exc),
        "file": traceback.extract_tb(exc.__traceback__)[-1].filename,
        "line": traceback.extract_tb(exc.__traceback__)[-1].lineno,
        "root_cause": "Unknown",
        "severity": "high"
    }

try:
    # code that might raise an exception
    x = 1 / 0
except Exception as e:
    error_dict = handle_exception(e)
    print(error_dict)