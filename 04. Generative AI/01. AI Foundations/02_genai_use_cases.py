# 02 — Gen AI use cases in software
# Run: python 02_genai_use_cases.py

USE_CASES = {
    "Developer tools": ["Code completion", "Refactoring suggestions", "Test generation"],
    "Business apps": ["Support chatbots", "Document Q&A", "Email drafts"],
    "Data work": ["Summarization", "Classification", "Entity extraction"],
    "Creative": ["Marketing copy", "Image generation", "Storyboards"],
}

if __name__ == "__main__":
    for category, examples in USE_CASES.items():
        print(f"\n{category}:")
        for ex in examples:
            print(f"  - {ex}")
