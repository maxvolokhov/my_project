from selenium.webdriver.common.by import By


from utilities.ui_utilities.base_page import BasePage


class ApplePodcastsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __text = (By.XPATH, '//h2[contains(text(), "Millions of shows. ")]')

    __drop_down_locator = (By.XPATH, '//button[@id="accordion-item-8-button"]')

    __link_transition = (By.XPATH, '//a[@data-analytics-title="learn more about podcaster resources"]')

    __expected_url = 'https://podcasters.apple.com/'

    def is_text_displayed(self):
        return self.is_displayed(self.__text)

    def drop_down_click(self):
        self.click(self.__drop_down_locator)
        return self

    def go_by_link(self):
        self.click(self.__link_transition)
        return self

    def url_assert(self):
        return self.__expected_url
