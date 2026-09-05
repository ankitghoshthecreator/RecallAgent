from ingestion.loader import load_documents
from ingestion.chunker import chunk_text
from graph.builder import GraphBuilder


DATA_DIR = r"D:\contextRag\data\raw"


def main():

    # -----------------------------
    # 1. Load documents
    # -----------------------------

    documents = load_documents(DATA_DIR)

    # -----------------------------
    # 2. Create chunks
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
    # 3. Build knowledge graph
    # -----------------------------

    graph_builder = GraphBuilder()

    graph = graph_builder.build(chunks)

    # -----------------------------
    # 4. Display graph
    # -----------------------------

    graph.show()

    neighbors = graph.get_neighbors("Rahul Sharma")

    print("\nRahul Sharma neighbors:")
    print("=" * 60)

    for neighbor in neighbors:
        print(
            f"Rahul Sharma "
            f"--{neighbor['relation']}--> "
            f"{neighbor['node']}"
        )

    paths = graph.find_paths(
        start_node="Rahul Sharma",
        max_hops=2
    )

    print("\n2-hop paths from Rahul Sharma:")
    print("=" * 60)

    for path in paths:

        print("\nPATH")

        for step in path:
            print(
                f"{step['source']} "
                f"--{step['relation']}--> "
                f"{step['target']}"
            )


if __name__ == "__main__":
    main()