class KnowledgeGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = set()

    def add_node(
        self,
        node_id: str,
        node_type: str,
        name: str
    ):
        if node_id not in self.nodes:
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
        edge = (
            source,
            relation,
            target
        )

        self.edges.add(edge)

    def get_neighbors(
            self,
            node_name: str
    ) -> list[dict]:

        neighbors = []

        for source, relation, target in self.edges:

            if source == node_name:
                neighbors.append({
                    "node": target,
                    "relation": relation
                })

        return neighbors

    def find_paths(
            self,
            start_node: str,
            max_hops: int = 2
    ) -> list[list[dict]]:

        paths = []

        def dfs(
                current_node: str,
                path: list[dict],
                depth: int
        ):

            if depth == max_hops:
                paths.append(path)
                return

            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                step = {
                    "source": current_node,
                    "relation": neighbor["relation"],
                    "target": neighbor["node"]
                }

                dfs(
                    neighbor["node"],
                    path + [step],
                    depth + 1
                )

        dfs(
            start_node,
            [],
            0
        )

        return paths

    def show(self):

        print("\nNODES")
        print("=" * 60)

        for node in self.nodes.values():
            print(
                f"{node['id']} "
                f"[{node['type']}] "
                f"→ {node['name']}"
            )

        print("\nEDGES")
        print("=" * 60)

        for source, relation, target in sorted(self.edges):

            print(
                f"{source} "
                f"--{relation}--> "
                f"{target}"
            )