from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __apple_id_locator = (By.XPATH, '//h2[@tabindex="-1" and text() = "Check out with your Apple ID"]')
    __frame_locator = (By.CSS_SELECTOR, '#aid-auth-widget-iFrame')

    def frame(self):
        self.switch_to_frame(self.__frame_locator)
        return self

    def validate_presence(self):
        return self.is_displayed(self.__apple_id_locator)
