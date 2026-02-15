from markitdown import MarkItDown

converter = MarkItDown()

def convert_to_markdown(input_path: str) -> str:
    """Convert docx to markdown using markitdown."""
    md = converter.convert(input_path)
    return md.text_content

def clean_markdown(md_text: str, text_split_string: str) -> str:
    """Clean the markdown by splitting it at a specific string and keeping the part after it."""
    idx = md_text.find(text_split_string) #TODO: what if the string is not found?
    clean = md_text[idx + len(text_split_string):].lstrip()
    return clean

def save_markdown(md_clean: str, output_path: str) -> None:
    """Save the markdown."""
    with open(output_path, "w") as f:
        f.write(md_clean)
