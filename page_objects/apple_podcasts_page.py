from selenium.webdriver.common.by import By
from utilities.ui_utilities.base_page import BasePage
import allure


class ApplePodcastsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __apple_podcasts_text_locator = (By.XPATH, '//h2[contains(text(), "Millions of shows. ")]')
    __drop_down_locator = (By.XPATH, '//button[@id="accordion-item-8-button"]')
    __link_transition = (By.XPATH, '//a[@data-analytics-title="learn more about podcaster resources"]')
    __expected_url = 'https://podcasters.apple.com/'
    __text_on_page = 'Millions of shows.\nMore ways to listen. Now we’re talking.'

    @allure.step
    @property
    def url_located(self):
        return self.__expected_url

    @allure.step
    @property
    def expected_text(self):
        return self.__text_on_page

    @allure.step
    def text_presence_check(self):
        return self.get_text(self.__apple_podcasts_text_locator)

    @allure.step
    def drop_down_click(self):
        self.click(self.__drop_down_locator)
        return self

    @allure.step
    def go_by_link(self):
        self.click(self.__link_transition)
        return self
