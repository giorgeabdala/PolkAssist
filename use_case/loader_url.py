from langchain.document_loaders import RecursiveUrlLoader
from bs4 import BeautifulSoup as Soup


class LoaderUrlUseCase:
    def __init__(self, url):
        self.url = url

##TextSplitter Defaults to RecursiveCharacterTextSplitter.
    #TODO: code bugado. Não está trazendo toda a arvore.
    def execute(self):
        loader = RecursiveUrlLoader(url=self.url, max_depth=5, extractor=lambda x: Soup(x, 'html.parser').text)
        return loader.load()
