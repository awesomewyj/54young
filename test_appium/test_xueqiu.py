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


    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        # self.driver.find_element(MobileBy.ID,"tv_agree").click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # el2.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # el3.send_keys("alibaba")
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("alibaba")

    def test_search_and_getprice(self):

        # self.driver.find_element(MobileBy.ID,"tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID,"name").click()
        assert float(self.driver.find_element(MobileBy.ID, "current_price").text) < 200

    def test_search_and_getprice_hk(self):
        # self.driver.find_element(MobileBy.ID,"tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        stock = (By.XPATH,"//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        price =(
            By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")
        assert float(self.driver.find_element(*price).text) < 200
        print(self.driver.find_element(*price).get_attribute("resourceId"))


    def test_scroll(self):  ##滑动
        size = self.driver.get_window_rect()
        TouchAction(self.driver).long_press( x= size["width"]*0.5,y = size["height"]*0.8)\
        .move_to( x= size["width"]*0.5,y = size["height"]*0.2).release().perform()

    def test_device(self):
        self.driver.background_app(5)



    def test_xpath(self):
        self.driver.find_element(
            By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]").click()


    def test_uiautomator(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView('
                    'new UiSelector().text("黄建平").instance(0));')
        self.driver.find_element(*scroll_to_element).click()




    def test_source(self):
        print(self.driver.page_source)

    def test_webview_negative(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text = '交易' and contains(@resource-id,'tab')] ").click()
        # sleep(10)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"A股开户").click()
        phone = (MobileBy.XPATH,"//*[@content-desc='请输入11位手机号']/..//android.widget.EditText")
        # phone = (MobileBy.ACCESSIBILITY_ID,"输入11位手机号")
        WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(phone))
        # print(self.driver.page_source)
        # self.driver.find_element(*phone).click()
        self.driver.find_element(*phone).send_keys("18682041663")


    def test_webview_context(self):  ####只有6.0可以
        self.driver.find_element(By.XPATH, "//*[@text = '交易' and contains(@resource-id,'tab')] ").click()
        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(1)
        WebDriverWait(self.driver,30).until(lambda x: len(self.driver.contexts)>1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.contexts)
        # sleep(5)
        # print(self.driver.page_source)
        # print(self.driver.find_element(By.CSS_SELECTOR,".trade_home_agu_3ki"))
        self.driver.find_element(By.CSS_SELECTOR,".trade_home_agu_3ki").click()
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     sleep(0.5)

        ##  可能会出现多窗口注意切换
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # sleep(10)

        ##元素可以找到的时候不代表可以被交互，需要用显示等待
        phone1 = (By.ID,"phone-number")
        WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(phone1))
        self.driver.find_element(*phone1).send_keys("18682041663")


    def test_performance(self):
        for p in self.driver.get_performance_data_types():
                print(p)

        print(self.driver.get_performance_data("com.xueqiu.android", "cpuinfo", 10))

    def test_record(self):
        ### srcpy 这个是更好的录屏
        pass


    def test_shell(self):
        result = self.driver.execute_script('mobile: shell',{
            'command':'echo',
            'args': ['arg1','arg2'],
            'includeStderr':True,
            'timeout':5000
        }

        )


    def teardown(self):
        sleep(20)
        self.driver.quit()
