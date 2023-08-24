from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AppleWatchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __size_locator = (By.XPATH, "//span[text() = '8']")
    __add_to_bag_locator = (By.XPATH, '//button[@id="add-to-cart"]')
    __add_item_to_bag = (By.XPATH, '//button[@data-autom="recommendations-addToBag-button"]')
    __item_bag_quantity = (By.XPATH, '//span[@class="globalnav-bag-badge-number" and text()="2"]')
    __expected_item_quantity = '2'

    @property
    def expected_item_quantity_return(self):
        return self.__expected_item_quantity

    def size_select(self):
        self.click(self.__size_locator)
        return self

    def add_to_bag(self):
        self.click(self.__add_to_bag_locator)
        return self

    def add_item_to_bag(self):
        self.click(self.__add_item_to_bag)
        return self

    def is_item_quantity_got(self):
        return self.get_text(self.__item_bag_quantity)
