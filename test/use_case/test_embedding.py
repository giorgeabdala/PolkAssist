import unittest

import embedding_minilm


class TestUseCaseEmbedding(unittest.TestCase):
    def test_embedding_minillm(self):
        usecase = embedding_minilm.EmbeddingMiniLMUseCase()
        embedding = usecase.get_embeddings()
        assert embedding is not None


if __name__ == '__main__':
    unittest.main()
