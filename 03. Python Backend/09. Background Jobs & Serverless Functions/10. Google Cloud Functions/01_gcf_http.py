# 01 — Google Cloud Functions HTTP entry
# Run: python 01_gcf_http.py

def hello_http(request):
    name = request.args.get("name", "World") if request.args else "World"
    return f"Hello, {name}!", 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    class FakeRequest:
        args = {"name": "Learner"}

    body, status, headers = hello_http(FakeRequest())
    print(status, body)
