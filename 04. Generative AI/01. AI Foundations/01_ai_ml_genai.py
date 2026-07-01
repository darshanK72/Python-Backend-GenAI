# 01 — AI, ML, DL, and Gen AI
# Run: python 01_ai_ml_genai.py

PARADIGMS = [
    ("Traditional programming", "Rules written by humans"),
    ("Machine Learning", "Patterns learned from data"),
    ("Deep Learning", "Neural networks with many layers"),
    ("Generative AI", "Models that create text, images, code, audio"),
]

if __name__ == "__main__":
    print("AI landscape:\n")
    for name, detail in PARADIGMS:
        print(f"  {name:24} {detail}")
