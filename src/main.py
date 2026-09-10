from ingestion.loader import load_documents
from ingestion.chunker import chunk_text

from graph.builder import GraphBuilder
from graph.retriever import GraphRetriever

from query.analyzer import QueryAnalyzer

from agent.retrieval_agent import RetrievalAgent


DATA_DIR = r"D:\contextRag\data\raw"


def main():

    # ============================================================
    # 1. Load documents
    # ============================================================

    documents = load_documents(DATA_DIR)

    print(f"Loaded documents: {len(documents)}")


    # ============================================================
    # 2. Chunk documents
    # ============================================================

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


    # ============================================================
    # 3. Build knowledge graph
    # ============================================================

    graph_builder = GraphBuilder()

    graph = graph_builder.build(chunks)


    # ============================================================
    # 4. Create graph retriever
    # ============================================================

    graph_retriever = GraphRetriever(graph)


    # ============================================================
    # 5. Create query analyzer
    # ============================================================

    analyzer = QueryAnalyzer()


    # ============================================================
    # 6. Create retrieval agent
    # ============================================================

    agent = RetrievalAgent(
        analyzer=analyzer,
        retriever=graph_retriever
    )


    # ============================================================
    # 7. Test queries
    # ============================================================

    queries = [

        "Which department is Rahul associated with?",

        "What project does Rahul work on?",

        "Who works on Atlas?"

    ]


    # ============================================================
    # 8. Run agent
    # ============================================================

    for query in queries:

        result = agent.run(query)


        print("\n" + "=" * 60)

        print("QUERY")
        print(query)


        # --------------------------------------------------------
        # Show agent plan
        # --------------------------------------------------------

        print("\nAGENT PLAN")
        print("-" * 60)

        plan = result["plan"]

        print("Strategy:", plan["strategy"])
        print("Entity:", plan["entity"])
        print("Target type:", plan["target_type"])
        print("Relation:", plan["relation"])
        print("Direction:", plan["direction"])
        print("Max hops:", plan["max_hops"])


        # --------------------------------------------------------
        # Show retrieved paths
        # --------------------------------------------------------

        print("\nRETRIEVED PATHS")
        print("-" * 60)

        paths = result["paths"]


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