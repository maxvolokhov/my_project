from page_objects.bag_page import BagPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class HomePodPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __add_to_bag_locator = (By.XPATH, '//span/button[@type="submit"]')
    __review_bag_locator = (By.XPATH, '//button[@name="proceed"]')

    @allure.step
    def add_homepod_to_bag(self):
        self.click(self.__add_to_bag_locator)
        return self

    @allure.step
    def check_your_bag(self):
        self.click(self.__review_bag_locator)
        return BagPage(self._driver)
