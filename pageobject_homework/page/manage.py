from selenium.webdriver.common.by import By

from pageobject_homework.page.base_page import BasePage


class Manage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"
    def load_picture(self):
        material_locator = (By.CSS_SELECTOR,'[href="#material/text"]')
        goto_picture_locator = (By.CSS_SELECTOR,'[href="#material/image"]')
        goto_upload_picture_locator =(By.CSS_SELECTOR,".js_upload_file_selector")
        upload_picture_locator = (By.ID,"js_upload_input")
        self.find(material_locator).click()
        self.find(goto_picture_locator).click()
        self.find(goto_upload_picture_locator).click()
        self.find(upload_picture_locator).send_keys("C:\\Users\\zzzaa\\Desktop\\9.jpg")


    def get_picture(self):
        first_picture_locator = (By.CSS_SELECTOR,".material_picCard_cnt_pic")
        return self.find(first_picture_locator).get_attribute("style")

