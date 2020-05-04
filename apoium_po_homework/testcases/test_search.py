from apoium_po_homework.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_quotes().goto_search().search("JD")