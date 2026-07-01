# 02 — Few-shot prompting template
# Run: python 02_few_shot_prompt.py

def build_sentiment_prompt(text: str) -> str:
    examples = """
Text: I love this product!
Sentiment: positive

Text: This broke on day one.
Sentiment: negative
"""
    return f"""Classify sentiment as positive, negative, or neutral.
{examples}
Text: {text}
Sentiment:"""


if __name__ == "__main__":
    for sample in ["Amazing support team!", "It is okay I guess."]:
        print(build_sentiment_prompt(sample))
        print("-" * 40)
