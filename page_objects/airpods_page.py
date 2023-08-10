from page_objects.bag_page import BagPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AirPodsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __air_pods_no_engraving = (By.XPATH, '//input[@value="noEngraving"]/following-sibling::label')
    __add_to_cart = (By.XPATH, '//button[@name="add-to-cart"]')
    __add_additional_item = (By.XPATH, '//span[@class="rc-addtobag-buttonlabel"]')
    __review_cart_locator = (By.XPATH, '//button[@name="proceed"]')

    def no_graving_click(self):
        self.click(self.__air_pods_no_engraving)
        return self

    def add_item_to_cart(self):
        self.click(self.__add_to_cart)
        return self

    def add_any_additional_item(self):
        self.click(self.__add_additional_item)
        return self

    def go_to_cart(self):
        self.click(self.__review_cart_locator)
        return BagPage(self._driver)
