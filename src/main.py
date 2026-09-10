from ingestion.loader import load_documents
from ingestion.chunker import chunk_text
from graph.builder import GraphBuilder
from query.analyzer import QueryAnalyzer
from graph.retriever import GraphRetriever


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
    # 2. Build graph
    # -------------------------

    graph_builder = GraphBuilder()
    graph = graph_builder.build(chunks)

    retriever = GraphRetriever(graph)


    # -------------------------
    # 3. Query analyzer
    # -------------------------

    analyzer = QueryAnalyzer()

    queries = [
        "Which department is Rahul associated with?",
        "What project does Rahul work on?",
        "Who works on Atlas?"
    ]


    # -------------------------
    # 4. Query-driven retrieval
    # -------------------------

    for query in queries:

        result = analyzer.analyze(query)

        result = analyzer.analyze(query)

        print("\n" + "=" * 60)
        print("Query:", query)
        print("Entity:", result["entity"])
        print("Target type:", result["target_type"])
        print("Relation:", result["relation"])
        print("Direction:", result["direction"])

        paths = retriever.retrieve(
            entity=result["entity"],
            target_type=result["target_type"],
            relation=result["relation"],
            max_hops=2,
            direction=result["direction"]
        )

        print("\nRetrieved paths:")

        if not paths:
            print("No paths found.")
            continue

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