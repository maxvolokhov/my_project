from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __review_bag_locator = (By.XPATH, '//form/button[@type="submit"]')

    @allure.step
    def review_bag(self):
        self.click(self.__review_bag_locator)
