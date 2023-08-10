from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AppleNewsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __try_one_month = (By.XPATH, '//button[@data-modal-target="upgrade"]')

    __ios_validate_locator = (By.XPATH, '//a[@href="https://support.apple.com/en-us/HT204204"]')

    def click_try_one_month(self):
        self.click(self.__try_one_month)
        return self

    def ios_validate(self):
        return self.is_displayed(self.__ios_validate_locator)
