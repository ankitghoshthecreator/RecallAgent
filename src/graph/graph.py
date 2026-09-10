class KnowledgeGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = set()


    # -------------------------
    # Add node
    # -------------------------

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


    # -------------------------
    # Add edge
    # -------------------------

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


    # -------------------------
    # Get outgoing neighbors
    # -------------------------

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


    # -------------------------
    # Get incoming neighbors
    # -------------------------

    def get_incoming_neighbors(
        self,
        node_name: str
    ) -> list[dict]:

        neighbors = []

        for source, relation, target in self.edges:

            if target == node_name:

                neighbors.append({
                    "node": source,
                    "relation": relation
                })

        return neighbors


    # -------------------------
    # Find arbitrary forward paths
    # -------------------------

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


    # -------------------------
    # Find paths to target type
    # -------------------------

    def find_paths_to_type(
        self,
        start_node: str,
        target_type: str,
        relation: str = "UNKNOWN",
        max_hops: int = 2,
        direction: str = "forward"
    ) -> list[list[dict]]:

        paths = []

        def dfs(
            current_node: str,
            path: list[dict],
            depth: int
        ):

            # -------------------------
            # Check target node
            # -------------------------

            if depth > 0:

                node = self.nodes.get(current_node)

                if node and node["type"] == target_type:

                    paths.append(path)

                    return


            # -------------------------
            # Stop at max hops
            # -------------------------

            if depth == max_hops:
                return


            # -------------------------
            # Forward traversal
            # -------------------------

            if direction == "forward":

                neighbors = self.get_neighbors(
                    current_node
                )

                for neighbor in neighbors:

                    # Filter by relation
                    if (
                        relation != "UNKNOWN"
                        and neighbor["relation"] != relation
                    ):
                        continue

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


            # -------------------------
            # Backward traversal
            # -------------------------

            elif direction == "backward":

                neighbors = self.get_incoming_neighbors(
                    current_node
                )

                for neighbor in neighbors:

                    # Filter by relation
                    if (
                        relation != "UNKNOWN"
                        and neighbor["relation"] != relation
                    ):
                        continue

                    # IMPORTANT:
                    #
                    # The stored relationship is:
                    #
                    # Rahul --WORKS_ON--> Atlas
                    #
                    # We are traversing it backwards,
                    # but the relationship itself remains:
                    #
                    # Rahul --WORKS_ON--> Atlas

                    step = {
                        "source": neighbor["node"],
                        "relation": neighbor["relation"],
                        "target": current_node
                    }

                    dfs(
                        neighbor["node"],
                        path + [step],
                        depth + 1
                    )


            else:

                raise ValueError(
                    "direction must be "
                    "'forward' or 'backward'"
                )


        dfs(
            start_node,
            [],
            0
        )

        return paths


    # -------------------------
    # Display graph
    # -------------------------

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

        for source, relation, target in sorted(
            self.edges
        ):

            print(
                f"{source} "
                f"--{relation}--> "
                f"{target}"
            )