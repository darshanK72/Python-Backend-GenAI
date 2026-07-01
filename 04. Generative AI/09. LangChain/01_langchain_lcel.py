# 01 — LangChain LCEL chain (requires API key)
# Run: python 01_langchain_lcel.py
# Install: pip install langchain langchain-openai

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass

if not os.getenv("OPENAI_API_KEY"):
    print("Set OPENAI_API_KEY in .env")
    raise SystemExit(1)

try:
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
except ImportError:
    print("Install: pip install langchain langchain-openai")
    raise SystemExit(1)

if __name__ == "__main__":
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a concise coding assistant."),
            ("user", "{question}"),
        ]
    )
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = prompt | model | StrOutputParser()
    print(chain.invoke({"question": "What is pytest used for?"}))
