from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __apple_id_locator = (By.XPATH, '//h2[@tabindex="-1" and text() = "Check out with your Apple ID"]')
    __frame_locator = (By.CSS_SELECTOR, '#aid-auth-widget-iFrame')

    @allure.step
    def frame(self):
        self.switch_to_frame(self.__frame_locator)
        return self

    @allure.step
    def is_item_presence_displayed(self):
        return self.is_displayed(self.__apple_id_locator)
