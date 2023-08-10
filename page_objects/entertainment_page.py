from selenium.webdriver.common.by import By
from page_objects.apple_podcasts_page import ApplePodcastsPage
from utilities.ui_utilities.base_page import BasePage


class EntertainmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __apple_podcasts_label = (By.XPATH, '//li[@class="chapternav-item chapternav-item-apple-podcasts"]/child::a')

    def apple_podcasts_find_and_click(self):
        self.click(self.__apple_podcasts_label)
        return ApplePodcastsPage(self._driver)
