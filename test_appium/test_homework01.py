# This sample code uses the Appium python client (python 2)
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable)

    def test_search_and_getprice02(self):

        # self.driver.find_element(MobileBy.ID,"tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID,"name").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='股票']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']").click()
        assert float(self.driver.find_element(MobileBy.ID, "stock_current_price").text) < 200


    def test_homework03(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='09988']/../../..//*[contains(@resource-id,'follow_btn')]").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']/../../..//*[@text = '加自选]')")
        self.driver.find_element(MobileBy.ID,"action_delete_text").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '阿里巴巴']").click()
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        res = self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='09988']/../../..//*[contains(@resource-id,'followed_btn')]").get_attribute("text")
        assert "已添加" == res



    def teardown(self):
        sleep(20)
        self.driver.quit()