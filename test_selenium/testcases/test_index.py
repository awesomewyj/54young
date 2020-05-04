from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.index import Index


class TestIndex:

    def setup(self):
        self.index = Index()


    def test_register(self):
        self.index.goto_register().register('测试学习')

        # self.driver.find_element(By.LINK_TEXT,"立即注册").click()
        # self.driver.find_element(By.ID,".corp_name").send_keys("测试学院")
        # self.driver.find_element(By.ID,".submit_btn").click()

    def test_login(self):
        register_page = self.index.goto_login().goto_registry().register("测吧（北京）科技有限公司")
        print(register_page.get_error_message())
        assert "请选择" in "|".join(register_page.get_error_message())


    def teardown(self):
        self.index.close()