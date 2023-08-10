from page_objects.italian_page import ItalianPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class LanguageSwitchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __italy = (By.XPATH, '//span[@lang="it-IT"]')

    def italy_select(self):
        self.click(self.__italy)
        return ItalianPage(self._driver)
