from ingestion.loader import load_documents
from ingestion.chunker import chunk_text
from graph.builder import GraphBuilder
from query.analyzer import QueryAnalyzer


DATA_DIR = r"D:\contextRag\data\raw"


def main():

    # -------------------------
    # 1. Load documents
    # -------------------------

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
                "text": chunk
            })

    print(f"Total chunks: {len(chunks)}")


    # -------------------------
    # 2. Build knowledge graph
    # -------------------------

    graph_builder = GraphBuilder()

    graph = graph_builder.build(chunks)


    # -------------------------
    # 3. Analyze queries
    # -------------------------

    analyzer = QueryAnalyzer()

    queries = [
        "Which department is Rahul associated with?",
        "What project does Rahul work on?",
        "Who works on Atlas?"
    ]

    for query in queries:

        result = analyzer.analyze(query)

        print("\nQuery:", query)
        print("Entity:", result["entity"])
        print("Target type:", result["target_type"])


    # -------------------------
    # 4. Test graph traversal
    # -------------------------

    department_paths = graph.find_paths_to_type(
        start_node="Rahul Sharma",
        target_type="DEPARTMENT",
        max_hops=2
    )

    print("\nPaths from Rahul Sharma to DEPARTMENT:")
    print("=" * 60)

    for path in department_paths:

        print("\nPATH")

        for step in path:

            print(
                f"{step['source']} "
                f"--{step['relation']}--> "
                f"{step['target']}"
            )


if __name__ == "__main__":
    main()