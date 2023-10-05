

import unittest
from typing import List

from use_case.embedding_minilm import EmbeddingMiniLMUseCase


class TestUseCaseEmbedding(unittest.TestCase):
    def test_embedding_minillm(self):
        use_case = EmbeddingMiniLMUseCase()
        embedding = use_case.get_embeddings()
        assert embedding is not None



if __name__ == '__main__':
    unittest.main()
