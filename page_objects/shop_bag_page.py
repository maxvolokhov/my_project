from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ShopBagPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __macbook_item_locator = (By.XPATH, '//a[text() = "15-inch MacBook Air with M2 chip - Midnight"]')
    __quantity_of_macbook_locator = (By.XPATH, '//option[@value="1"]')
    __remove_button_locator = (By.XPATH, '//button[@data-autom="bag-item-remove-button"]')
    __expected_text = 'Remove'

    @allure.step
    @property
    def expected_text_return(self):
        return self.__expected_text

    @allure.step
    def is_item_parameters_displayed(self):
        return self.is_displayed(self.__macbook_item_locator) and self.is_displayed(self.__quantity_of_macbook_locator)

    @allure.step
    def is_remove_item_got(self):
        return self.get_text(self.__remove_button_locator)
