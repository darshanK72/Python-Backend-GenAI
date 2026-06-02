# 04 — JSON request/response shape (API contract)
# Run: python 04_json_api_contract.py

import json

# Typical API response
response = {
    "success": True,
    "data": [
        {"id": 1, "name": "Asha", "marks": 88},
        {"id": 2, "name": "Ravi", "marks": 76},
    ],
    "error": None,
}

print(json.dumps(response, indent=2))

# Typical POST body
create_student = {"name": "Meera", "marks": 92, "city": "Mumbai"}
print("\nPOST body:", json.dumps(create_student))
