import unittest
from typing import List

import loader_url

class TestUseCaseLoaderUrl(unittest.TestCase):
    def test_loaderUrlUsecase(self):
        url = "https://wiki.polkadot.network/docs/learn-polkadot-host"
        use_case = loader_url.LoaderUrlUseCase()
        docs = use_case.execute(url)
        assert isinstance(docs, List)
        assert len(docs) > 0


if __name__ == '__main__':
    unittest.main()
