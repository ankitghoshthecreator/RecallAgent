
class QueryAnalyzer:

    # -------------------------
    # Detect target type
    # -------------------------

    def detect_target_type(self, query: str) -> str:

        query = query.lower()

        if "department" in query:
            return "DEPARTMENT"

        if "project" in query:
            return "PROJECT"

        if "who" in query:
            return "PERSON"

        return "UNKNOWN"

    # -------------------------
    # Detect entity
    # -------------------------

    def detect_entity(self, query: str) -> str:

        query = query.lower()

        if "rahul" in query:
            return "Rahul Sharma"

        if "atlas" in query:
            return "Atlas"

        if "mercury" in query:
            return "Mercury"

        if "orion" in query:
            return "Orion"

        return "UNKNOWN"

    # -------------------------
    # Detect traversal direction
    # -------------------------

    def detect_direction(self, query: str) -> str:

        query = query.lower()

        if "who works on" in query:
            return "backward"

        return "forward"

    # -------------------------
    # Analyze complete query
    # -------------------------

    def analyze(self, query: str) -> dict:

        return {
            "entity": self.detect_entity(query),
            "target_type": self.detect_target_type(query),
            "direction": self.detect_direction(query)
        }
