from ingestion.loader import load_documents
from ingestion.chunker import chunk_text


DATA_DIR = "data/raw"


def main():
    documents = load_documents(DATA_DIR)

    for document in documents:
        chunks = chunk_text(
            document["text"],
            chunk_size=20,
            chunk_overlap=5
        )

        print("=" * 60)
        print(f"Document: {document['document_id']}")
        print(f"Source: {document['source']}")

        for i, chunk in enumerate(chunks):
            print(f"\nChunk {i}:")
            print(chunk)


if __name__ == "__main__":
    main()