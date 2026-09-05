from query.analyzer import QueryAnalyzer


def main():

    analyzer = QueryAnalyzer()

    queries = [
        "Which department is Rahul associated with?",
        "What project does Rahul work on?",
        "Who works on Atlas?"
    ]

    for query in queries:

        target_type = analyzer.detect_target_type(query)

        print(f"\nQuery: {query}")
        print(f"Target type: {target_type}")


if __name__ == "__main__":
    main()