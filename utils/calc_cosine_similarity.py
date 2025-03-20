import numpy as np

def cosine_similarity(vec_a, vec_b):
    """Compute cosine similarity between two vectors."""
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))
