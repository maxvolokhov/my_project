from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ShopBagPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __macbook_item_locator = (By.XPATH, '//a[text() = "15-inch MacBook Air with M2 chip - Midnight"]')
    __quantity_of_macbook_locator = (By.XPATH, '//option[@value="1"]')
    __remove_button_locator = (By.XPATH, '//button[@data-autom="bag-item-remove-button"]')

    def are_items_displayed(self):
        return self.is_displayed(self.__macbook_item_locator) and self.is_displayed(self.__quantity_of_macbook_locator)

    def remove_item_displayed(self):
        return self.is_displayed(self.__remove_button_locator)
