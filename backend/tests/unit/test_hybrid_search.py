import pytest

from src.rag.calculations import bm25, cos_sim


class TestHybridSearch:

    def test_bm25_relevant_documents_score_higher(self):
        '''Document that contains query words should be scored higher'''
        docs = [
            'postgres is a relational database',
            'cats are cute animals'
        ]

        scores = list(bm25('postgres database', docs))
        assert scores[0] > scores[1]

    def test_bm25_length_normalization(self):
        '''Short document should be scored higher than long one'''
        docs = [
            'postgres is a relational database',
            'postgres' + 'random word' * 200
        ]
        scores = list(bm25('postgres', docs))
        assert scores[0] > scores[1]
    
    def test_cosine_similarity_identical_vectors_give_one(self):
        vec = [0.3, 0.6, 0.9]
        assert cos_sim(vec, vec) == pytest.approx(1.0)

    def test_cosine_similarity_orthogonal_vectors_give_zero(self):
        assert cos_sim([0, 1], [1, 0]) == pytest.approx(0)

    def test_cosine_similarity_zero_vector_does_not_crash(self):
        '''Dividing by zero'''
        assert cos_sim([0, 0], [1, 1]) is None