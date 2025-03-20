# embedding_service.py

import requests
import numpy as np

class EmbeddingService:
    """Handles batch requests for code snippet embeddings via the OpenAI API."""
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model

    def get_embeddings_batch(self, texts):
        response = requests.post(
            "https://api.openai.com/v1/embeddings",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"input": texts, "model": self.model}
        )
        if response.status_code != 200:
            raise Exception("Error obtaining embeddings: " + response.text)
        data = response.json()
        embeddings = [np.array(item['embedding']) for item in data['data']]
        return embeddings
