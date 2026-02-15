from src.data_processing.pdf_to_docx import pdf_to_docx
from src.data_processing.docx_to_markdown import (
    convert_to_markdown,
    clean_markdown,
    save_markdown,
)

pdf_path = "data/pdf/northstar.pdf"
docx_path = "data/docx/northstar.docx"
md_path = "data/markdown/northstar.md"


def data_processing_pipeline():
    """Run the data processing pipeline"""
    pdf_to_docx(pdf_path, docx_path)
    md_text = convert_to_markdown(docx_path)
    clean_md = clean_markdown(md_text, "Bilag 2: Fiktiv vidensbase")
    save_markdown(clean_md, md_path)


if __name__ == "__main__":
    data_processing_pipeline()
