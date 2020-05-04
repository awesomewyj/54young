from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from apoium_po_homework.page.base_page import BasePage
from apoium_po_homework.page.quotes import Quotes

from test_appium.page.profile import Profile
from test_appium.page.search import Search


class Main(BasePage):
    _driver: WebDriver
    def __init__(self,driver):
        self._driver = driver


    # def goto_search_page(self):
    #     # self.find(MobileBy.ID, "tv_search").click()
    #     self.steps("../page/steps.yaml")
    #     return Search(self._driver)
    #
    # def goto_stocks(self):
    #     pass
    #
    # def goto_trade(self):
    #     pass
    # #
    # def goto_profile(self):
    #     self.find(By.XPATH, "//*[@text='我的']").click()
    #     return Profile(self._driver)
    #
    # def goto_messages(self):
    #     pass

    #
    def goto_quotes(self):
        self.steps("../page/main.yaml")
        return Quotes(self._driver)