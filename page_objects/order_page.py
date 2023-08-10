from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __bag_counter_locator = (By.XPATH, '//a[@aria-label="Shopping Bag with item count : 1"]')

    def counter_checker(self):
        return self.is_displayed(self.__bag_counter_locator)
