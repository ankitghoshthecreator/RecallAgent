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
    # Detect relationship
    # -------------------------

    def detect_relation(self, query: str) -> str:

        query = query.lower()

        if "works on" in query or "work on" in query:
            return "WORKS_ON"

        if "maintained by" in query:
            return "MAINTAINED_BY"

        if "leads" in query:
            return "LEADS"

        if "collaborates with" in query:
            return "COLLABORATES_WITH"

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
            "relation": self.detect_relation(query),
            "direction": self.detect_direction(query)
        }
