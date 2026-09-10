from graph.graph import KnowledgeGraph


class GraphRetriever:

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph


    def retrieve(
        self,
        entity: str,
        target_type: str,
        relation: str,
        max_hops: int = 2,
        direction: str = "forward"
    ) -> list[list[dict]]:

        return self.graph.find_paths_to_type(
            start_node=entity,
            target_type=target_type,
            relation=relation,
            max_hops=max_hops,
            direction=direction
        )
