from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact

class Tools(BasePage):

    def add_member(self):
        pass

    def goto_material_library(self):
        self.find((By.PARTIAL_LINK_TEXT, "素材库")).click()
        return self

    def bouns(self):
        pass
