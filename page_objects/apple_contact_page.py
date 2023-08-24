from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AppleContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    countries_to_check = ['United States', 'Canada', 'Mexico']

    def generate_country_locator(self, country_name):
        return (By.XPATH, f'//div[@class="country"]/*[contains(text(), "{country_name}")]')

    def is_country_displayed(self, country_name):
        locator = self.generate_country_locator(country_name)
        return self.is_displayed(locator)
