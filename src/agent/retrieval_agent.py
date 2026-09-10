from query.analyzer import QueryAnalyzer
from graph.retriever import GraphRetriever


class RetrievalAgent:

    def __init__(
        self,
        analyzer: QueryAnalyzer,
        retriever: GraphRetriever
    ):
        self.analyzer = analyzer
        self.retriever = retriever

    # -------------------------
    # Create retrieval plan
    # -------------------------

    def create_plan(self, query: str) -> dict:

        analysis = self.analyzer.analyze(query)

        entity = analysis["entity"]
        target_type = analysis["target_type"]
        relation = analysis["relation"]
        direction = analysis["direction"]

        # Decide maximum hops
        if target_type == "DEPARTMENT":
            max_hops = 2
        else:
            max_hops = 1

        # Currently we only use graph retrieval.
        # Later the agent will be able to choose
        # between graph and vector retrieval.
        strategy = "graph"

        return {
            "strategy": strategy,
            "entity": entity,
            "target_type": target_type,
            "relation": relation,
            "direction": direction,
            "max_hops": max_hops
        }

    # -------------------------
    # Execute retrieval plan
    # -------------------------

    def run(self, query: str) -> dict:

        plan = self.create_plan(query)

        # -------------------------
        # Execute graph retrieval
        # -------------------------

        paths = self.retriever.retrieve(
            entity=plan["entity"],
            target_type=plan["target_type"],
            relation=plan["relation"],
            max_hops=plan["max_hops"],
            direction=plan["direction"]
        )

        # -------------------------
        # Return result
        # -------------------------

        return {
            "query": query,
            "plan": plan,
            "paths": paths
        }