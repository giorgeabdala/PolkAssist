from langchain.text_splitter import RecursiveCharacterTextSplitter

#number of characters in each division
CHUNK_SIZE = 1500
#the maximum overlap between chunks
CHUNK_OVERLAP = 150


class SplitDocUseCase:

    def execute(self, doc):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )

        chunks = text_splitter.split_documents(doc)
        return chunks

