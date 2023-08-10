from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AppleWatchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __size_locator = (By.XPATH, "//span[text() = '8']")
    __add_to_bag_locator = (By.XPATH, '//button[@id="add-to-cart"]')
    __add_item_to_bag = (By.XPATH, '//button[@data-autom="recommendations-addToBag-button"]')
    __item_bag_quantity = (By.XPATH, '//a[@aria-label="Shopping Bag with item count : 2"]')

    def size_select(self):
        self.click(self.__size_locator)
        return self

    def add_to_bag(self):
        self.click(self.__add_to_bag_locator)
        return self

    def add_item_to_bag(self):
        self.click(self.__add_item_to_bag)
        return self

    def item_quantity_check(self):
        return self.is_displayed(self.__item_bag_quantity)
