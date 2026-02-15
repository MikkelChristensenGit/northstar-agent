import json
from langchain_community.document_loaders import TextLoader


def markdown_to_documents(md_path: str):
    """Load markdown file as Langchain Documents with TextLoader."""
    loader = TextLoader(md_path)
    docs = loader.load()
    return docs

def save_chunks(chunks):
    """Save the chunks as a jsonl file."""
    with open("data/chunks/chunks.jsonl", "w") as f:    
        for chunk in chunks:
            json.dump({"text": chunk.page_content, "metadata": chunk.metadata}, f)
            f.write("\n")