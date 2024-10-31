from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class AirPods2Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __atb_button = (By.XPATH, '//button[@id="add-to-cart"]')
    __quantity_locator = (By.XPATH, '//select[@data-autom="item-quantity-dropdown"]')
    __value_locator = (By.XPATH, '//option[@value="3"]')
    __value_validator = (By.XPATH, '//div[@data-autom="bagtotalvalue" and text()="$387.00"]')

    @allure.step
    def atb_click(self):
        self.click(self.__atb_button)
        return self

    @allure.step
    def selector_click(self):
        self.click(self.__quantity_locator)
        return self

    @allure.step
    def value_click(self):
        self.click(self.__value_locator)
        return self

    @allure.step
    def is_increased_price_displayed(self):
        return self.is_displayed(self.__value_validator)
