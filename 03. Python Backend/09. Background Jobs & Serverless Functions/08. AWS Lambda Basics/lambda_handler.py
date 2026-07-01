# AWS Lambda handler pattern
# Deploy: zip with handler.py + dependencies


def handler(event, context):
    name = (event or {}).get("name", "World")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": f'{{"message": "Hello, {name}!"}}',
    }
