# 03 — Azure OpenAI and other providers (overview)
# Run: python 03_cloud_providers.py

PROVIDERS = {
    "OpenAI": "OPENAI_API_KEY — api.openai.com",
    "Azure OpenAI": "AZURE_OPENAI_ENDPOINT + AZURE_OPENAI_API_KEY",
    "Anthropic": "ANTHROPIC_API_KEY — Claude models",
    "Google": "GEMINI_API_KEY — Gemini models",
    "Local": "Ollama — no cloud key, runs on your machine",
}

if __name__ == "__main__":
    print("Common LLM providers:\n")
    for name, detail in PROVIDERS.items():
        print(f"  {name:16} {detail}")
