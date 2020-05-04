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


class Apidemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        caps["skipServerInstallation"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)




    def test_toast(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView('
                    'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView('
                    'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()


        # self.driver.find_element(MobileBy.XPATH,"//*[@contains = 'MAKE A POPUP']").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()  ###accessbility  专门用来指向 content-desc
        self.driver.find_element(MobileBy.XPATH,"//*[@text = 'Search']").click()

        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

        assert "Clicked popup menu item Search" in toast
        assert "Clicked" in toast




    def teardown(self):
        sleep(20)
        self.driver.quit()
