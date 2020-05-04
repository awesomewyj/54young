from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFirstone:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def wait(self,timeout,method):
        WebDriverWait(self.driver,timeout).until(method)

    def test_homework(self):
        element = (By.PARTIAL_LINK_TEXT, '2020年 第一季度招聘贴')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # # todo：显式等待
        element_select = (By.CSS_SELECTOR,".toc-container > .btn")
        self.wait(10,expected_conditions.element_to_be_clickable(element_select))
        self.driver.find_element(*element_select).click()
        sleep(2)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"华东地区").click()
    ###切换窗口
    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"第六届中国互联网测试开发大会").click()
        print(self.driver.window_handles)
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        element = (By.LINK_TEXT, "演讲申请")
        self.wait(10,expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def test_js(self):
        for code in [
            'return document.title',
            'return document.querySelector(".active").className',
            'return JSON.stringify(performance.timing)'
        ]:

            result1 = self.driver.execute_script(code)
            print(result1)

    def teaedown_method(self):
        sleep(10)
        self.driver.quit()
