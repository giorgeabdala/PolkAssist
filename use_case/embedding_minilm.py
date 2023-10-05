from langchain.embeddings import SentenceTransformerEmbeddings

SENTENCE_EMBEDDING_MODEL = "all-MiniLM-L6-v2"


class EmbeddingMiniLMUseCase:

    def get_embeddings(self):
        return SentenceTransformerEmbeddings(model_name=SENTENCE_EMBEDDING_MODEL)
