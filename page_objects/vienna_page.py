from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ViennaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __store_address = (By.XPATH, '//address[text()="Kärntner Straße 11"]')

    @allure.step
    def is_address_is_located(self):
        return self.is_displayed(self.__store_address)
