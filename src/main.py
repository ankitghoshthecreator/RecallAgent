from ingestion.loader import load_documents
from ingestion.chunker import chunk_text
from retrieval.embedder import Embedder
from retrieval.vector_search import VectorSearch


DATA_DIR = r"D:\contextRag\data\raw"


def main():

    # -----------------------------
    # 1. Load documents
    # -----------------------------

    documents = load_documents(DATA_DIR)

    # -----------------------------
    # 2. Chunk documents
    # -----------------------------

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
                "text": chunk
            })

    print(f"Total chunks: {len(chunks)}")

    # -----------------------------
    # 3. Create embeddings
    # -----------------------------

    embedder = Embedder()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedder.embed_documents(texts)

    print(f"Embedding shape: {embeddings.shape}")

    # -----------------------------
    # 4. Create vector search
    # -----------------------------

    vector_search = VectorSearch(
        embeddings=embeddings,
        chunks=chunks
    )

    # -----------------------------
    # 5. User query
    # -----------------------------

    query =  "Which department is Rahul associated with?"

    # -----------------------------
    # 6. Embed query
    # -----------------------------

    query_embedding = embedder.embed_query(query)

    # -----------------------------
    # 7. Search
    # -----------------------------

    results = vector_search.search(
        query_embedding=query_embedding,
        top_k=3
    )

    # -----------------------------
    # 8. Display results
    # -----------------------------

    print("\n" + "=" * 60)
    print(f"QUERY: {query}")
    print("=" * 60)

    for i, result in enumerate(results):

        print(f"\nResult {i + 1}")
        print(f"Score: {result['score']:.4f}")
        print(f"Source: {result['chunk']['source']}")
        print(f"Chunk ID: {result['chunk']['chunk_id']}")
        print(f"Text: {result['chunk']['text']}")


if __name__ == "__main__":
    main()