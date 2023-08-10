from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class BusinessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __enterprise_locator = (By.XPATH, '//a[@class="nav-link typography-nav-link"][@href="/business/enterprise/"]')
    __pdf_locator = (By.XPATH, '//a[@href="/business/docs/site/AAW_Productivity.pdf"]')
    __pdf_check = (By.XPATH, '//embed[@type="application/pdf"]')

    def enterprise_click(self):
        self.click(self.__enterprise_locator)
        return self

    def pdf_click(self):
        self.click(self.__pdf_locator)
        return self

    def pdf_check(self):
        return self.is_displayed(self.__pdf_check)