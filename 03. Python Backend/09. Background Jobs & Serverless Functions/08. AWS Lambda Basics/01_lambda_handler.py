# 01 — AWS Lambda handler structure
# Run: python 01_lambda_handler.py

from lambda_handler import handler

if __name__ == "__main__":
    event = {"name": "Learner"}
    context = {"function_name": "demo", "request_id": "local-1"}
    response = handler(event, context)
    print("Lambda response:", response)
