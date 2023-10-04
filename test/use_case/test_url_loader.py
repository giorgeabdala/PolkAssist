import unittest
from typing import List

from use_case.loader_url import LoaderUrlUseCase
from langchain.schema.document import Document


class TestUseCaseLoaderUrl(unittest.TestCase):
    def test_loaderUrlUsecase(self):
        url = "https://wiki.polkadot.network/docs/learn-polkadot-host"
        use_case = LoaderUrlUseCase()
        docs = use_case.execute(url)
        assert isinstance(docs, List)
        assert len(docs) > 0


if __name__ == '__main__':
    unittest.main()
