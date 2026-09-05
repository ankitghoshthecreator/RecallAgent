import re


class RelationshipExtractor:

    def extract(self, text: str) -> list[dict]:
        relationships = []

        # -----------------------------------------
        # WORKS_ON
        #
        # Example:
        # Rahul currently works on the Atlas project.
        # Arjun works on the Atlas project.
        # -----------------------------------------

        pattern = (
            r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
            r"\s+(?:currently\s+)?works\s+on\s+"
            r"(?:the\s+)?([A-Z][A-Za-z]+)"
            r"(?:\s+project)?"
        )

        for match in re.finditer(pattern, text):
            relationships.append({
                "source": match.group(1),
                "relation": "WORKS_ON",
                "target": match.group(2)
            })

        # -----------------------------------------
        # MAINTAINED_BY
        #
        # Example:
        # Atlas is maintained by the Research and
        # Development department.
        # -----------------------------------------

        pattern = (
            r"([A-Z][A-Za-z]+)"
            r"\s+is\s+maintained\s+by\s+the\s+"
            r"(.+?)\s+department"
        )

        for match in re.finditer(pattern, text):
            relationships.append({
                "source": match.group(1),
                "relation": "MAINTAINED_BY",
                "target": match.group(2)
            })

        # -----------------------------------------
        # LEADS
        #
        # Example:
        # Priya provides technical leadership for
        # the Atlas project.
        # -----------------------------------------

        pattern = (
            r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
            r"\s+provides\s+(?:technical|financial)\s+"
            r"leadership\s+for\s+(?:the\s+)?"
            r"([A-Z][A-Za-z]+)"
        )

        for match in re.finditer(pattern, text):
            relationships.append({
                "source": match.group(1),
                "relation": "LEADS",
                "target": match.group(2)
            })

        # -----------------------------------------
        # COLLABORATES_WITH
        #
        # Example:
        # Rahul collaborates regularly with
        # Priya Mehta and Arjun Kapoor.
        # -----------------------------------------

        pattern = (
            r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
            r"\s+collaborates\s+(?:regularly\s+)?with\s+"
            r"(.+?)(?:\s+on|\.)"
        )

        for match in re.finditer(pattern, text):

            source = match.group(1).strip()
            targets = match.group(2).strip()

            # Handle multiple people:
            # "Priya Mehta and Arjun Kapoor"
            people = re.split(r"\s+and\s+", targets)

            for person in people:
                relationships.append({
                    "source": source,
                    "relation": "COLLABORATES_WITH",
                    "target": person.strip()
                })

        return relationships