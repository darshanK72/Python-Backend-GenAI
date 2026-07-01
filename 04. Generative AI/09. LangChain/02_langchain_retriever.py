# 02 — LangChain with Chroma retriever
# Run: python 02_langchain_retriever.py
# Install: pip install langchain langchain-openai langchain-chroma chromadb

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
    from langchain_chroma import Chroma
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnablePassthrough
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
except ImportError:
    print("Install: pip install langchain langchain-openai langchain-chroma chromadb")
    raise SystemExit(1)

DOCS = [
    "FastAPI uses Pydantic for request validation.",
    "Django includes an admin panel and ORM out of the box.",
]

if __name__ == "__main__":
    vectorstore = Chroma.from_texts(DOCS, OpenAIEmbeddings(model="text-embedding-3-small"))
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    prompt = ChatPromptTemplate.from_template(
        "Answer using context only.\n\nContext: {context}\n\nQuestion: {question}"
    )
    model = ChatOpenAI(model="gpt-4o-mini")

    def format_docs(docs):
        return "\n".join(d.page_content for d in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    print(chain.invoke("How does FastAPI validate requests?"))
