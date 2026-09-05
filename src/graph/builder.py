from graph.graph import KnowledgeGraph
from graph.entity import EntityNormalizer
from graph.extractor import RelationshipExtractor


class GraphBuilder:

    def __init__(self):

        self.graph = KnowledgeGraph()

        self.extractor = RelationshipExtractor()

        self.normalizer = EntityNormalizer()

    def get_node_type(self, name: str) -> str:

        people = {
            "Rahul Sharma",
            "Priya Mehta",
            "Arjun Kapoor",
            "Sneha Iyer",
            "Vikram Rao",
            "Meera Nair",
            "Karan Shah"
        }

        projects = {
            "Atlas",
            "Mercury",
            "Orion"
        }

        departments = {
            "Research and Development",
            "Finance",
            "Customer Operations"
        }

        if name in people:
            return "PERSON"

        if name in projects:
            return "PROJECT"

        if name in departments:
            return "DEPARTMENT"

        return "UNKNOWN"

    def add_relationships(self, text: str):

        relationships = self.extractor.extract(text)

        for relationship in relationships:

            source = self.normalizer.normalize(
                relationship["source"]
            )

            target = self.normalizer.normalize(
                relationship["target"]
            )

            source_type = self.get_node_type(source)
            target_type = self.get_node_type(target)

            # Add source node
            self.graph.add_node(
                node_id=source,
                node_type=source_type,
                name=source
            )

            # Add target node
            self.graph.add_node(
                node_id=target,
                node_type=target_type,
                name=target
            )

            # Add relationship
            self.graph.add_edge(
                source=source,
                relation=relationship["relation"],
                target=target
            )

    def build(self, chunks: list[dict]) -> KnowledgeGraph:

        for chunk in chunks:

            self.add_relationships(
                chunk["text"]
            )

        return self.graph