from ingestion.loader import load_documents
from ingestion.chunker import chunk_text
from retrieval.embedder import Embedder


DATA_DIR = r"D:\contextRag\data\raw"


def main():
    documents = load_documents(DATA_DIR)

    chunks = []

    for document in documents:
        document_chunks = chunk_text(
            document["text"],
            chunk_size=100,
            chunk_overlap=20
        )

        for i, chunk in enumerate(document_chunks):
            chunks.append({
                "chunk_id": f"{document['document_id']}_chunk_{i}",
                "document_id": document["document_id"],
                "source": document["source"],
                "text": chunk,
            })

    print(f"Total chunks: {len(chunks)}")

    embedder = Embedder()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedder.embed_documents(texts)

    print(f"Embedding shape: {embeddings.shape}")
    print(f"First embedding:\n{embeddings[0]}")


if __name__ == "__main__":
    main()