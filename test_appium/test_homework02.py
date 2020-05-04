# This sample code uses the Appium python client (python 2)
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
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
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True
        caps["chromedriverExecutable"] = "C:\\Users\\zzzaa\\Downloads\\chromedriver\\chromedriver.exe"  ####安卓6.0用的driver

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable)

    def test_webview_context(self):  ####只有6.0可以
        self.driver.find_element(By.XPATH, "//*[@text = '交易' and contains(@resource-id,'tab')] ").click()
        WebDriverWait(self.driver,30).until(lambda x: len(self.driver.contexts)>1)
        self.driver.switch_to.context(self.driver.contexts[-1])  ###切换至最后一个
        # WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.driver.find_element(By.CSS_SELECTOR,".trade_home_xueying_SJY")))
        # sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,".trade_home_xueying_SJY").click()

        ##  可能会出现多窗口注意切换
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # sleep(10)

        ##元素可以找到的时候不代表可以被交互，需要用显示等待
        phone1 = (By.CSS_SELECTOR,"[placeholder='请输入手机号']")
        WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(phone1))
        self.driver.find_element(*phone1).send_keys("18682041663")
        phone2 = (By.CSS_SELECTOR, "[placeholder='请输入验证码']")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(phone2))
        self.driver.find_element(*phone2).send_keys("1234")


        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(By.XPATH,"//*[@index = '1' and contains(@resource-id,'action_bar_close')]").click()

    def teardown(self):
        sleep(20)
        self.driver.quit()
