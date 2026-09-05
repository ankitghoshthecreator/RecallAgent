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

    def detect_target_type(self, query: str) -> str | None:

        query_lower = query.lower()

        for keyword, node_type in self.question_to_type.items():

            if keyword in query_lower:
                return node_type

        return None