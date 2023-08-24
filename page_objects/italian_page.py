from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ItalianPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __italian_word = (By.XPATH, "//span/span[contains(text(), 'Intrattenimento')]")
    __italian_text = 'Intrattenimento'

    @property
    def italian_text_check(self):
        return self.__italian_text

    def italian_word_displayed(self):
        return self.get_text(self.__italian_word)
