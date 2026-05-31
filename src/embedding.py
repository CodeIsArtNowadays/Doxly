from sentence_transformers import SentenceTransformer

from src.calculations import cos_sim
from src.bm25 import bm25

semantic_model = SentenceTransformer('all-MiniLM-L6-v2')


class Vector:
    def __init__(self, text, metadata=None):
        self.text = text
        vec = semantic_model.encode(text)
        self.vec = vec
        self.metadata = metadata
    
    def __str__(self):
        return f'{self.text} | Vec {self.vec.shape}'
        
    def __repr__(self):
        return f'{self.text}'
    

class VectorStorage:
    
    def __init__(self, text=None):
        self.vectors = []
        self.chunks = []
        
        if text:
            chunks = self._chunking_char(text)
            for chunk in chunks:
                self.add_vector(Vector(chunk))
    
    def _chunking_char(self, text, size=300, overlap=50):
        res = []
        step = size - overlap
        for i in range(0, len(text), step):
            res.append(text[i:i+size])
        self.chunks = res
        return res
    
    def add_vector(self, vector: Vector):
        self.vectors.append(vector)
    
    def sort(self, query_vector):
        score = sorted(self.vectors, key=lambda x: cos_sim(query_vector, x.vec), reverse=True)
        return score
    
    def bm25_search(self, query):
        res = bm25(query, self.chunks)
        print(res)
        
    
    def search(self, query, k=1):
        v_query = semantic_model.encode(query)
        return self.sort(v_query)[:k]


