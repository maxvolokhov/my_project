from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AirPods2Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __atb_button = (By.XPATH, '//button[@id="add-to-cart"]')
    __quantity_locator = (By.XPATH, '//select[@data-autom="item-quantity-dropdown"]')
    __value_locator = (By.XPATH, '//option[@value="3"]')
    __value_validator = (By.XPATH, '//div[@data-autom="bagtotalvalue" and text()="$387.00"]')

    def atb_click(self):
        self.click(self.__atb_button)
        return self

    def selector_click(self):
        self.click(self.__quantity_locator)
        return self

    def value_click(self):
        self.click(self.__value_locator)
        return self

    def price_validator(self):
        return self.is_displayed(self.__value_validator)
