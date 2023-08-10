from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class TopBooksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __book_locator = (By.XPATH, '//div[@class="targeted-link__target" and text()="Tom Lake"]')
    __price_locator = (By.XPATH, '//li[@class="inline-list__item inline-list__item--slashed"]/span[text()="$14.99"]')

    def book_select(self):
        self.click(self.__book_locator)
        return self

    def price_is_displayed(self):
        return self.is_displayed(self.__price_locator)
