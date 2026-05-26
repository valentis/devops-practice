import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class ItemRecommender:
    def __init__(self):
        self.similarity_matrix = None
        self.item_ids = []

    def fit(self, interaction_matrix: np.ndarray, item_ids: list):
        self.similarity_matrix = cosine_similarity(interaction_matrix.T)
        self.item_ids = item_ids

    def recommend(self, liked_item_idx: int, top_k: int = 10) -> list:
        scores = self.similarity_matrix[liked_item_idx]
        top_indices = np.argsort(scores)[::-1][1 : top_k + 1]
        return [self.item_ids[i] for i in top_indices]
