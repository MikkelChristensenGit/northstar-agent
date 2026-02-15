import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Initialization

# 1) set up embedding model for query embedding
embeddings = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL"))

# 2) connect to existing Qdrant collection
vectorstore = QdrantVectorStore.from_existing_collection(
    url=os.getenv("QDRANT_URL"),
    collection_name=os.getenv("QDRANT_COLLECTION"),
    embedding=embeddings,
)

# 3) LLM 
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def retrieve_context(question: str, k: int = 3) -> list:
    """Retrieve top k documents for a question."""
    return vectorstore.similarity_search(question, k=k)

def build_context(docs: list) -> str:
    """Format documents into a single context string with separator."""
    return "\n\n---\n\n".join(doc.page_content for doc in docs)

def generate_answer(question: str, k: int = 3) -> dict:
    """Generate an answer and return sources."""
    docs = retrieve_context(question, k=k)
    context = build_context(docs)
    prompt = (
        "You are a helpful assistant. Answer the question using only the context.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n"
        "Answer:"
    )
    response = llm.invoke(prompt)
    return {"answer": response.content}

