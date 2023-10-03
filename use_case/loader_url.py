from langchain.document_loaders import WebBaseLoader


class LoaderUrlUseCase:

##TextSplitter Defaults to RecursiveCharacterTextSplitter.
    def execute(self, url):
        loader = WebBaseLoader(url)
        docs = loader.load()
        return docs
