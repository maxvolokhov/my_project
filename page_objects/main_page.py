from selenium.webdriver.common.by import By
from page_objects.apple_news_page import AppleNewsPage
from page_objects.apple_podcasts_page import ApplePodcastsPage
from page_objects.apple_vision_page import AppleVisionPage
from page_objects.apple_wallet_page import AppleWalletPage
from page_objects.business_page import BusinessPage
from page_objects.retail_page import RetailPage
from utilities.ui_utilities.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __entertainment_label = (By.XPATH, '//a[@href="/entertainment/"]')
    __apple_store_label = (By.XPATH, '//a[@href="/us/shop/goto/account"]')
    __apple_contact = (By.XPATH, '//a[@href="/contact/"]')
    __iphone_buy = (By.XPATH, '//a[@href="/us/shop/goto/buy_iphone/iphone_14_pro"]')
    __language_locator = (By.XPATH, '//a[@href="/choose-country-region/"]')
    __search_button = (By.XPATH, '//a[@id="globalnav-menubutton-link-search"]')
    __search_line = (By.XPATH, '//li[@data-topnav-flyout-label = "Search apple.com"]')
    __search_hover = (By.XPATH, '//input[@placeholder="Search"]')
    __bag_locator = (By.XPATH, '//a[@href="/us/shop/goto/bag"]')
    __empty_text_locator = (By.XPATH, '''//h2[@style="--r-globalnav-flyout-item-number: 0;"
     and text() = 'Your Bag is empty.']''')
    __find_store = (By.XPATH, '//a[@class="ac-gf-directory-column-section-link" and @href="/retail/"]')
    __wallet_locator = (By.XPATH, '//a[@data-analytics-title="wallet" and text() = "Wallet"]')
    __apple_news_locator = (By.XPATH, '//a[@class="ac-gf-directory-column-section-link"] [@href="/apple-news/"]')
    __apple_podcasts_locator = (By.XPATH, '//a[@class="ac-gf-directory-column-section-link"][@href="/apple-podcasts/"]')
    __apple_business = (By.XPATH, '//a[@href="/business/"]')
    __apple_vision_locator = (By.XPATH, '//a[@aria-label="Vision"]')
    __expected_text = 'Your Bag is empty.'

    @allure.step
    @property
    def expected_text_return(self):
        return self.__expected_text

    @allure.step
    def entertainment_find_and_click(self):
        self.click(self.__entertainment_label)

    @allure.step
    def apple_store_find_and_click(self):
        self.click(self.__apple_store_label)

    @allure.step
    def apple_contact(self):
        self.click(self.__apple_contact)

    @allure.step
    def buy_iphone(self):
        self.click(self.__iphone_buy)

    @allure.step
    def language_click(self):
        self.click(self.__language_locator)

    @allure.step
    def search_button_click(self):
        self.click(self.__search_button)
        return self

    @allure.step
    def search_line_click(self):
        self.click(self.__search_line)
        return self

    @allure.step
    def set_search_input(self, input1):
        self.send_keys(self.__search_hover, input1)

    @allure.step
    def click_bag_locator(self):
        self.click(self.__bag_locator)

    @allure.step
    def is_bag_empty_got(self):
        return self.get_text(self.__empty_text_locator)

    @allure.step
    def store_click(self):
        self.click(self.__find_store)
        return RetailPage(self._driver)

    @allure.step
    def go_to_wallet(self):
        self.click(self.__wallet_locator)
        return AppleWalletPage(self._driver)

    @allure.step
    def go_apple_news(self):
        self.click(self.__apple_news_locator)
        return AppleNewsPage(self._driver)

    @allure.step
    def podcasts_transition(self):
        self.click(self.__apple_podcasts_locator)
        return ApplePodcastsPage(self._driver)

    @allure.step
    def business_transition(self):
        self.click(self.__apple_business)
        return BusinessPage(self._driver)

    @allure.step
    def apple_vision_transition(self):
        self.click(self.__apple_vision_locator)
        return AppleVisionPage(self._driver)
