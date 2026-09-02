from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: list[str]):
        """
        Convert multiple document chunks into embeddings.

        Args:
            texts: List of text chunks.

        Returns:
            NumPy array containing embeddings.
        """
        return self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def embed_query(self, query: str):
        """
        Convert a user query into an embedding.

        Args:
            query: User's question.

        Returns:
            NumPy array containing the query embedding.
        """
        return self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )