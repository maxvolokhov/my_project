from page_objects.gift_card_page import GiftCardPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AppleStorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __accessories_locator = (By.XPATH, '//div/a[@href="/shop/accessories/all" and text()="Accessories"]')
    __search_line_locator = (By.XPATH, '//input[@name="search"]')
    __search_result = (By.XPATH, '//div[@class="rf-accessories-section-resultcount rf-serp-resultcount as-l-container"]')
    __gift_locator = (By.XPATH, '//a[@href="/shop/gift-cards" and text()="Apple Gift Card"]')
    __buy_locator = (By.XPATH, '//a[@href="/shop/buy-giftcard/giftcard"]')

    def accessories_click(self):
        self.click(self.__accessories_locator)
        return self

    def insert_search_line(self, search_input, press_enter=False):
        self.send_keys(self.__search_line_locator, search_input, press_enter=press_enter)
        return self

    def is_search_result_displayed(self):
        return self.is_displayed(self.__search_result)

    def apple_gift_transition(self):
        self.click(self.__gift_locator)
        return self

    def click_buy(self):
        self.click(self.__buy_locator)
        return GiftCardPage(self._driver)
