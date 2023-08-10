from page_objects.vienna_page import ViennaPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class RetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_line_locator = (By.XPATH, '//input[@type="text"]')
    __text_validate = (By.XPATH, '//p[@class="store-detail-heading-name-status" and text()="Opens at 10:00 a.m."]')
    __drop_down_list = (By.XPATH, '//ul[@id="store-search-stores"]')
    __us_drop_down = (By.XPATH, '//select[@id="dropdown"]')
    __austria_locator = (By.XPATH, '//option[@value="en_AT"]')
    __vienna_store = (By.XPATH, '//a[@href="/at/retail/kaerntnerstrasse/"]')

    def set_apple_store(self, apple_store_name):
        self.send_keys(self.__search_line_locator, apple_store_name)
        return self

    def select_from_list(self):
        self.click(self.__drop_down_list)
        return self

    def store_work_time(self):
        return self.is_displayed(self.__text_validate)

    def click_us_drop_down(self):
        self.click(self.__us_drop_down)
        return self

    def select_austria(self):
        self.click(self.__austria_locator)
        return self

    def austria_store_click(self):
        self.click(self.__vienna_store)
        return ViennaPage(self._driver)
