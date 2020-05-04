from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFirstone:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")##无窗口模式
        options.add_argument("disable-gpu")
        options.add_argument("--window-size=1536, 824)")

        ##使用已经存在的浏览器窗口
        options.debugger_address("127.0.0.1:922")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://testerhome.com/")
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def wait(self,timeout,method):
        WebDriverWait(self.driver,timeout).until(method)

    def test_firstone(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        # todo：显式等待
        ##尽量使用CSS定位
        element = (By.LINK_TEXT, "霍格沃兹测试学院")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        # WebDriverWait(self.driver,10).until(lambda x:self.driver.find_element(element)>1)
        self.wait(10,expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # self.driver.find_element(By.CSS_SELECTOR, "[data-name=霍格沃兹测试学院]").click()
        # todo:隐式游戏
        # self.driver.find_element(By.CSS_SELECTOR, ".topic-22359 .title > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".topic:nth-child(1) .title a").click()

    ###切换窗口
    def test_mtsc(self):
        self.driver.get("https://testerhome.com/topics/21805")
        # self.driver.set_window_size(1536, 824)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        print(self.driver.window_handles)
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        element = (By.LINK_TEXT, "演讲申请")
        #截图  发现是分辨率的问题
        self.driver.save_screenshot("1.png")

        self.wait(10, expected_conditions.presence_of_all_elements_located(element))
        self.driver.find_element(*element).click()

    def test_js(self):
        for code in [
            'return document.title',
            'return document.querySelector(".active").className',
            'return JSON.stringify(performance.timing)'
        ]:

            result1 = self.driver.execute_script(code)

    def teaedown_method(self):
        sleep(10)
        self.driver.quit()
