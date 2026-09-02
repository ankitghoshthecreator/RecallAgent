def chunk_text(
    text: str,
    chunk_size: int = 100,
    chunk_overlap: int = 20
) -> list[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: Input document text.
        chunk_size: Maximum number of words in each chunk.
        chunk_overlap: Number of words shared between consecutive chunks.

    Returns:
        List of text chunks.
    """

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks