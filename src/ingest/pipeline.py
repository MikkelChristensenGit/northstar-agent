import os
from pathlib import Path

from dotenv import load_dotenv

from src.ingest.utils import markdown_to_documents, save_chunks

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

def ingest_pipeline():
    """Run the ingest pipeline."""
    docs = markdown_to_documents("/Users/mchr/Documents/pfa/data/markdown/northstar.md")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50) # 10 % overlap
    chunks = splitter.split_documents(docs)
    save_chunks(chunks) # save chunks as jsonl

    embeddings = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL"))

    QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url=os.getenv("QDRANT_URL"),
        collection_name=os.getenv("QDRANT_COLLECTION"),
    )

    print(f"Ingested {len(chunks)} chunks into Qdrant collection '{os.getenv('QDRANT_COLLECTION')}'")

if __name__ == "__main__":
    ingest_pipeline()
