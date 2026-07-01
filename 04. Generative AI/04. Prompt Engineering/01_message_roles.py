# 01 — System, user, and assistant messages
# Run: python 01_message_roles.py

MESSAGES = [
    {"role": "system", "content": "You are a concise Python tutor."},
    {"role": "user", "content": "What is a list comprehension?"},
    {"role": "assistant", "content": "A compact way to build lists from iterables."},
]

if __name__ == "__main__":
    print("Chat message roles:\n")
    for msg in MESSAGES:
        print(f"  [{msg['role']:10}] {msg['content']}")
