# 03 — LangChain vs raw OpenAI SDK
# Run: python 03_langchain_overview.py

if __name__ == "__main__":
    print("Use raw OpenAI SDK when:")
    print("  - Simple chat or completion calls")
    print("  - You want minimal dependencies")
    print("\nUse LangChain when:")
    print("  - Chains, retrievers, agents, memory")
    print("  - Swapping models/providers with less rewrite")
    print("  - Building RAG pipelines quickly")
