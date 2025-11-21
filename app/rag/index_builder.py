import os
from pathlib import Path
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from app.config import settings


INDEX_PATH = "app/data/faiss_index"

def load_docs() -> List[Document]:
    docs_dir = Path(settings.DOCS_PATH)
    documents: List[Document] = []

    for path in docs_dir.glob("**/*"):
        if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
            loader = TextLoader(str(path), encoding="utf-8")
            docs = loader.load()
            # optionally set metadata
            for d in docs:
                d.metadata["source"] = str(path)
            documents.extend(docs)

    return documents


def build_index():
    docs = load_docs()
    print(f"Loaded {len(docs)} documents")

    embeddings = OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(docs, embeddings)

    os.makedirs(INDEX_PATH, exist_ok=True)
    vectorstore.save_local(INDEX_PATH)
    print(f"Index saved to {INDEX_PATH}")


if __name__ == "__main__":
    build_index()
