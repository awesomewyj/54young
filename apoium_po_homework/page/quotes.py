from apoium_po_homework.page.base_page import BasePage
from apoium_po_homework.page.search import Search


class Quotes(BasePage):

    def goto_search(self):
        self.steps("../page/quotes.yaml")
        return Search(self._driver)
