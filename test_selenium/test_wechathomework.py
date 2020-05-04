from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWwechat:
    def setup_method(self):
        options = Options()
        ##使用已经存在的浏览器窗口
        options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_work(self):
        self.driver.find_element(By.ID,"menu_contacts").click()
        # self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_item").click()
        # sleep(10)
        # self.driver.find_element(By.CSS_SELECTOR,".js_has_member div:nth-child(1) .js_add_member").click()
        WebDriverWait(self.driver, 15).until(self.wait_element)
        self.driver.find_element(By.ID,"username").send_keys("abcd")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("78955ghjbj")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("12345678910")

        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
    #
    def wait_element(self,aaa):
        size = len(self.driver.find_elements(By.ID,"username"))
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR,".js_has_member div:nth-child(1) .js_add_member").click()
        return size >= 1
