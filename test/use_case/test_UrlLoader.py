import unittest
from typing import List

from use_case.loader_url import LoaderUrlUseCase
from langchain.schema.document import Document


class MyTestCase(unittest.TestCase):
    def test_loaderUrlUsecase(self):
        url = "https://docs.python.org/3.9/"
        use_case = LoaderUrlUseCase(url=url)
        docs = use_case.execute()
        assert isinstance(docs, List)
        print(docs)
        assert len(docs) > 0


if __name__ == '__main__':
    unittest.main()
