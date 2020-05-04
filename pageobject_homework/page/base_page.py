from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    def __init__(self, reuse=False):

        if reuse:
            options = webdriver.ChromeOptions()
                ##使用已经存在的浏览器窗口
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
        else:
            self._driver = webdriver.Chrome()

        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.implicitly_wait(5)



    def find(self, by, locator=""):
        # ActionChains(self._driver).move_to_element(self.find(xxxxxx))
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)
