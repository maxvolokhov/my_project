from page_objects.bag_page import BagPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AppleTvPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __wifi_version_locator = (By.XPATH, '//input[@value="wifitv64gb"]/following-sibling::label')
    __put_in_bag = (By.XPATH, '//button[@name="add-to-cart"]')
    __proceed_button = (By.XPATH, '//button[@value="proceed"]')

    def wifi_version_click(self):
        self.click(self.__wifi_version_locator)
        return self

    def put_item_in_bag(self):
        self.click(self.__put_in_bag)

    def click_on_proceed_button(self):
        self.click(self.__proceed_button)
        return BagPage(self._driver)
