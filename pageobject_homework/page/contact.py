from time import sleep

from selenium.webdriver.common.by import By

from pageobject_homework.page.base_page import BasePage


class Contact(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    def add_member(self):
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        # $('.ww_radio[value="2"]')
        gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        mobile_locator = (By.NAME, 'mobile')
        save_locator = (By.CSS_SELECTOR,".js_btn_save")
        self.find(name_locator).send_keys("awesome")
        self.find(acctid_locator).send_keys("seveniruby")
        self.find(gender_locator).click()
        self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        # self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find(mobile_locator).send_keys("13838381438")
        self.find(save_locator).click()
        return self

    def get_memeber(self):
        first_member_locator = (By.CSS_SELECTOR,"#member_list tr:nth-child(2) td:nth-child(2)")
        return  self.find(first_member_locator).get_attribute("title")
        ####获取特定的属性值

