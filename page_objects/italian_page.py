from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ItalianPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __italian_word = (By.XPATH, "//span/span[contains(text(), 'Intrattenimento')]")

    def is_word_displayed(self):
        return self.is_displayed(self.__italian_word)
