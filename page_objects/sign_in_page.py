from selenium.webdriver.common.by import By
from utilities.ui_utilities.base_page import BasePage


class SigninPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __frame_locator = (By.CSS_SELECTOR, '#aid-auth-widget-iFrame')

    __apple_id_field = (By.XPATH, '//div/input[@type="text"]')

    __login_button = (By.XPATH, '//i[@class= "shared-icon icon_sign_in"]')

    __password_field = (By.CSS_SELECTOR, '#password_text_field')

    __text_after_login = (By.CSS_SELECTOR, '#errMsg')

    def frame(self):
        self.switch_to_frame(self.__frame_locator)
        return self

    def set_apple_id(self, apple_id_value):
        self.send_keys(self.__apple_id_field, apple_id_value)
        return self

    def login_click(self):
        self.click(self.__login_button)

    def set_password(self, password):
        self.send_keys(self.__password_field, password)
        return self

    def is_text_login_displayed(self):
        return self.is_displayed(self.__text_after_login)
