from appium.webdriver.common.mobileby import MobileBy

from apoium_po_homework.page.base_page import BasePage


class Search(BasePage):
    _name_locator = (MobileBy.ID, "name")

    def search(self, key: str):
        # self.find(MobileBy.ID, "search_input_text").send_keys(key)
        # self.find(self._name_locator).click()
        #
        self._params = {}
        self._params["value2"] = key
        self.steps("../page/search.yaml")

        return self