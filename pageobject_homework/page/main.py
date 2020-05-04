from selenium.webdriver.common.by import By

from pageobject_homework.page.base_page import BasePage
from pageobject_homework.page.contact import Contact


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_addmember(self):
        goto_addmember_locator = (By.CSS_SELECTOR,'[node-type="addmember"]')
        self.find(goto_addmember_locator).click()
        return Contact(reuse=True)
