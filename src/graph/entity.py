class EntityNormalizer:

    def __init__(self):
        self.aliases = {
            "Rahul": "Rahul Sharma",
            "Arjun": "Arjun Kapoor",
            "Priya": "Priya Mehta",
            "Sneha": "Sneha Iyer",
            "Vikram": "Vikram Rao",
            "Atlas": "Atlas",
            "Mercury": "Mercury",
            "Orion": "Orion",
            "Research and Development": "Research and Development",
            "Finance": "Finance",
            "Customer Operations": "Customer Operations",
        }

    def normalize(self, name: str) -> str:
        name = name.strip()

        return self.aliases.get(name, name)