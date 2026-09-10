class QueryAnalyzer:

    def __init__(self):
        self.question_to_type = {
            "department": "DEPARTMENT",
            "departments": "DEPARTMENT",
            "project": "PROJECT",
            "projects": "PROJECT",
            "employee": "PERSON",
            "employees": "PERSON",
            "person": "PERSON",
            "people": "PERSON",
            "who": "PERSON"
        }

        self.entity_aliases = {
            "rahul": "Rahul Sharma",
            "rahul sharma": "Rahul Sharma",
            "arjun": "Arjun Kapoor",
            "arjun kapoor": "Arjun Kapoor",
            "priya": "Priya Mehta",
            "priya mehta": "Priya Mehta",
            "sneha": "Sneha Iyer",
            "sneha iyer": "Sneha Iyer",
            "vikram": "Vikram Rao",
            "vikram rao": "Vikram Rao",

            "atlas": "Atlas",
            "mercury": "Mercury",
            "orion": "Orion",

            "research and development": "Research and Development",
            "finance": "Finance",
            "customer operations": "Customer Operations"
        }

    def detect_target_type(self, query: str) -> str | None:
        query_lower = query.lower()

        for keyword, node_type in self.question_to_type.items():
            if keyword in query_lower:
                return node_type

        return None

    def detect_entity(self, query: str) -> str | None:
        query_lower = query.lower()

        for alias, entity in self.entity_aliases.items():
            if alias in query_lower:
                return entity

        return None

    def analyze(self, query: str) -> dict:
        return {
            "entity": self.detect_entity(query),
            "target_type": self.detect_target_type(query)
        }