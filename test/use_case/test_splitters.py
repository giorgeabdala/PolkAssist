import unittest
from use_case.loader_url import LoaderUrlUseCase
from use_case.split_doc import SplitDocUseCase


class TestUseCaseSplitDoc( unittest.TestCase):

    def test_split_doc(self):
        url = "https://wiki.polkadot.network/docs/learn-polkadot-host"
        loader_use_case = LoaderUrlUseCase()
        doc = loader_use_case.execute(url)

        split_use_case = SplitDocUseCase()
        split_docs = split_use_case.execute(doc)

        assert len(split_docs) >= 4







if __name__ == '__main__':
    unittest.main()
