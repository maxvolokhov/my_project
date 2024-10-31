from page_objects.support_apple_page import SupportApplePage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AppleWalletPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __drop_down_selector = (By.XPATH, '//button[@aria-controls="accordion-item-2-tray"]')
    __learn_more_locator = (By.XPATH, '//p/a[@href="https://support.apple.com/en-us/HT209495"]')

    @allure.step
    def drop_down_click(self):
        self.click(self.__drop_down_selector)
        return self

    @allure.step
    def learn_more_click(self):
        self.click(self.__learn_more_locator)
        return SupportApplePage(self._driver)
