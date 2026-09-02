import numpy as np


class VectorSearch:
    def __init__(self, embeddings: np.ndarray, chunks: list[dict]):
        """
        Args:
            embeddings: Matrix of document embeddings.
                        Shape: (number_of_chunks, embedding_dimension)

            chunks: Metadata and text corresponding to each embedding.
        """

        self.embeddings = embeddings
        self.chunks = chunks

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 3
    ) -> list[dict]:

        # Calculate similarity between query and every chunk
        scores = self.embeddings @ query_embedding

        # Get indices of highest scores
        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for index in top_indices:
            results.append({
                "chunk": self.chunks[index],
                "score": float(scores[index])
            })

        return results