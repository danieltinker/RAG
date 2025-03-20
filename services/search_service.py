# search.py

from utils.calc_cosine_similarity import cosine_similarity

class SearchService:
    """Provides functionality to search for similar code snippets via embeddings."""
    def __init__(self, embedding_service):
        self.embedding_service = embedding_service

    def search(self, query, index, top_k=3):
        query_embedding = self.embedding_service.get_embeddings_batch([query])[0]
        scores = []
        for item in index:
            score = cosine_similarity(query_embedding, item['embedding'])
            scores.append((score, item))
        scores.sort(key=lambda x: x[0], reverse=True)
        

        return scores[:top_k]
