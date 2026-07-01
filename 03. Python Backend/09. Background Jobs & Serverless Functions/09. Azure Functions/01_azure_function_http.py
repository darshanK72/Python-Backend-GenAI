# 01 — Azure Functions HTTP trigger (Python v2 model)
# Run: python 01_azure_function_http.py

SAMPLE = '''
import azure.functions as func

app = func.FunctionApp()

@app.route(route="hello", methods=["GET"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")
    return func.HttpResponse(f"Hello, {name}!")
'''

if __name__ == "__main__":
    print("Azure Functions — HTTP trigger pattern:\n")
    print(SAMPLE.strip())
    print("\nInstall: pip install azure-functions")
    print("Run locally: func start")
