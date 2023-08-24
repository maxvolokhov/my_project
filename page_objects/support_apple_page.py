from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class SupportApplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __text_validation = (By.XPATH, '//h2[@id="expresstransit"]')

    def is_text_displayed(self):
        return self.is_displayed(self.__text_validation)
