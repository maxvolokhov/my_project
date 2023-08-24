from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()


class AppleVisionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __notify_me_locator = (By.XPATH, '//button[@aria-label="Notify me, Apple Vision Pro availability"]')
    __input_hover = (By.XPATH, '//input[@type="email"]')
    __submit_locator = (By.XPATH, '//button[@aria-label="Notify me when Apple Vision Pro is available"]')
    __notify_validate_locator = (By.XPATH, '//span[@id="notifyUnknownError"]')
    __expected_text = 'An unknown error occurred. Please try again.'

    @property
    def expected_text_return(self):
        return self.__expected_text

    def notify_me_click(self):
        self.click(self.__notify_me_locator)
        return self

    def make_input_field_active_click(self):
        self.click(self.__input_hover)
        return self

    def set_email(self):
        self.send_keys(self.__input_hover, fake.email())
        return self

    def submit_button_click(self):
        self.click(self.__submit_locator)
        return self

    def is_notify_got(self):
        return self.get_text(self.__notify_validate_locator)
