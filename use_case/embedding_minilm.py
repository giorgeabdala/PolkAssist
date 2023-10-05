from langchain.embeddings import SentenceTransformerEmbeddings

SENTENCE_EMBEDDING_MODEL="all-MiniLM-L6-v2"
class EmbeddingMiniLMUseCase:

##TODO: não funcionnando
    def execute(self):
        embedding = SentenceTransformerEmbeddings(model_name=SENTENCE_EMBEDDING_MODEL)
        return embedding

