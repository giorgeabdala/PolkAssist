import unittest
import loader_url
import split_doc


class TestUseCaseSplitDoc( unittest.TestCase):

    def test_split_doc(self):
        url = "https://wiki.polkadot.network/docs/learn-polkadot-host"
        loader_use_case = loader_url.LoaderUrlUseCase()
        doc = loader_use_case.execute(url)

        split_use_case = split_doc.SplitDocUseCase()
        split_docs = split_use_case.execute(doc)

        assert len(split_docs) >= 4



if __name__ == '__main__':
    unittest.main()
