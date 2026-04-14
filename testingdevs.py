import requests
import traceback

def buggy_function():
    a = 5
    b = "10"
    return a + b  # This will crash

try:
    buggy_function()

except Exception as e:
    error_data = {
        "error_type": type(e).__name__,
        "message": str(e),
        "file": "app/utils/calculator.py",
        "line": 42,
        "stack_trace": traceback.format_exc(),
        "severity": "high",
        "timestamp": "2026-04-14"
    }

    requests.post(
        "http://localhost:5678/webhook/bug-detector",
        json=error_data
    )