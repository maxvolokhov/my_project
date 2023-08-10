from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AppleContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __usa_contact = (By.XPATH, '''//div[@class="country"]/*[contains(text(), 'United States')]''')
    __canada_contact = (By.XPATH, '''//div[@class="country"]/*[contains(text(), 'Canada')]''')
    __mexico_contact = (By.XPATH, '''//div[@class="country"]/*[contains(text(), 'Mexico')]''')

    def text_country(self):
        return self.is_displayed(self.__usa_contact and self.__canada_contact and self.__mexico_contact)
