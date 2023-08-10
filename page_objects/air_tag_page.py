from page_objects.bag_page import BagPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AirTagPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __skip_locator = (By.XPATH, '//span[@class="form-selector-title" and text() = "Skip engraving"]')
    __add_to_bag_locator = (By.XPATH, '//span[@class="label" and text() = "Add to Bag"]')
    __review_bag_locator = (By.XPATH, '//button[@name="proceed"]')

    def skip_engraving(self):
        self.click(self.__skip_locator)
        return self

    def add_airtag_to_bag(self):
        self.click(self.__add_to_bag_locator)
        return self

    def review_bag_click(self):
        self.click(self.__review_bag_locator)
        return BagPage(self._driver)
