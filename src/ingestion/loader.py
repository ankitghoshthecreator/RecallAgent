from pathlib import Path

"""
Load all text documents from a directory.

Args:
    data_dir: Path containing raw documents.

Returns:
    A list of dictionaries containing document metadata and text.
"""

def load_documents(data_dir: str) -> list[dict]:
    documents = []

    data_path = Path(data_dir)

    for file_path in data_path.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "document_id": file_path.stem,
            "source": file_path.name,
            "text": text,
        })

    return documents