import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self,data):
        # self.driver.find_element(By.ID, "corp_name").click
        time.sleep(5)
        self._driver.find_element(By.ID, "corp_name").send_keys(data)
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def get_error_message(self):
        result = []
        for element in self._driver.find_elements(By.CSS_SELECTOR,".js_error_msg"):

            result.append(element.text)

        return result





