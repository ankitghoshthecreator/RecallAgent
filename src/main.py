from graph.extractor import RelationshipExtractor


def main():

    extractor = RelationshipExtractor()

    text = """
    Rahul Sharma currently works on the Atlas project.
    Rahul collaborates regularly with Priya Mehta and Arjun Kapoor
    on technical design and project planning.

    Atlas is maintained by the Research and Development department.

    Priya Mehta provides technical leadership for the Atlas project.
    """

    relationships = extractor.extract(text)

    for relationship in relationships:
        print(relationship)


if __name__ == "__main__":
    main()