from page_objects.top_books_page import TopBooksPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AppleBooksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __browse_page_locator = (By.XPATH, '//span[@class="icon-copy"]')

    @allure.step
    def go_to_browse_page(self):
        self.click(self.__browse_page_locator)
        return TopBooksPage(self._driver)
