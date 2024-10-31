from page_objects.order_page import OrderPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class BuyIphonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __iphone_select = (By.XPATH, '//input[@id="20eafef0-2978-11ee-8c2e-c18eeddf789c"]')
    __new = (By.XPATH, '//span/span[contains(text(), "iPhone 14 Pro Max")]')
    __iphone_color = (By.XPATH, "//img/following-sibling::span[text() = 'Deep Purple']")
    __iphone_storage = (By.XPATH, '//input[@data-autom="dimensionCapacity1tb"]')
    __no_trade_in = (By.XPATH, '//label[@id = "noTradeIn_label"]')
    __buy_iphone_option = (By.XPATH, '//label[@id = "e35ecc70-2afc-11ee-831f-2fa8a3df01f1_label"]')
    __carrier_locator = (By.XPATH, '//label[@id = "8199d5f1-2af9-11ee-831f-2fa8a3df01f1_label"]')
    __apple_coverage = (By.XPATH, '//label[@id = "applecareplus_59_noapplecare_label"]')
    __add_to_bag = (By.XPATH, '//button[@class="button button-block"]')

    @allure.step
    def iphone_14_pro_exist(self):
        return self.is_displayed(self.__iphone_select)

    @allure.step
    def new_click(self):
        self.click(self.__new)
        return self

    @allure.step
    def color_select(self):
        self.click(self.__iphone_color)
        return self

    @allure.step
    def storage_select(self):
        self.click(self.__iphone_storage)

    @allure.step
    def no_trade_in_select(self):
        self.click(self.__no_trade_in)

    @allure.step
    def buy_iphone_option(self):
        self.click(self.__buy_iphone_option)

    @allure.step
    def carrier_select(self):
        self.click(self.__carrier_locator)

    @allure.step
    def coverage_select(self):
        self.click(self.__apple_coverage)

    @allure.step
    def add_iphone_to_bag(self):
        self.click(self.__add_to_bag)
        return OrderPage(self._driver)
