class KnowledgeGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(
        self,
        node_id: str,
        node_type: str,
        name: str
    ):
        self.nodes[node_id] = {
            "id": node_id,
            "type": node_type,
            "name": name
        }

    def add_edge(
        self,
        source: str,
        relation: str,
        target: str
    ):
        self.edges.append({
            "source": source,
            "relation": relation,
            "target": target
        })

    def show(self):

        print("\nNODES")
        print("=" * 50)

        for node in self.nodes.values():
            print(node)

        print("\nEDGES")
        print("=" * 50)

        for edge in self.edges:
            print(edge)