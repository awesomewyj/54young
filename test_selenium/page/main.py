from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact
from test_selenium.page.message import Message
from test_selenium.page.tools import Tools


class Main(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def download(self):
        pass

    def import_user(self,path):
        self.find((By.PARTIAL_LINK_TEXT, "导入通讯录")).click()
        # self.find((By.LINK_TEXT, "批量导入")).click()
        self.find(By.ID, "js_upload_file_input").send_keys(path)
        self.find((By.ID, "submit_csv")).click()
        self.find((By.ID, "reloadContact")).click()
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass


    def get_message(self):
        return ["aaa","bbb"]

    def goto_tools(self):
        self.find((By.PARTIAL_LINK_TEXT, "管理工具")).click()
        return Tools(reuse = True)


    def add_member(self):
        locator=(By.LINK_TEXT, '添加成员')
        # self.find(locator).click()
        self._driver.execute_script("arguments[0].click();", self.find(locator))
        return Contact(reuse = True)

    def send_message(self):
        locator = (By.LINK_TEXT,"消息群发")
        self.find(locator).click()
        return Message(reuse = True)

