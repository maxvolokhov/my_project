from page_objects.shop_bag_page import ShopBagPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class MacbookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __select_button_locator = (By.XPATH, '//button[@data-autom="proceed-15inch-best"]')
    __add_to_bag_locator = (By.XPATH, '//button[@value="add-to-cart"]')
    __review_bag_locator = (By.XPATH, '//button[@data-autom="proceed"]')

    def macbook_select(self):
        self.click(self.__select_button_locator)
        return self

    def add_macbook_to_bag(self):
        self.click(self.__add_to_bag_locator)
        return self

    def review_bag_click(self):
        self.click(self.__review_bag_locator)
        return ShopBagPage(self._driver)
