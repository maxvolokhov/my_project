from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class BagPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __remove_item_locator = (By.XPATH, '''//button[@id="shoppingCart.items.
    item-24874f80-5d59-44db-8177-8969a8284a8e.delete"]''')
    __remove_button_loctor_for_remove = (By.XPATH, '//button[@data-autom="bag-item-remove-button"]')
    __emptiness_assert_locator = (By.XPATH, '//h1[@class="rs-bag-header"]')
    __total_items_in_cart = (By.XPATH, '//a[@aria-label="Shopping Bag with item count : 2"]')
    __add_apple_care_locator = (By.XPATH, '//button[@data-autom="bag-inlineattach-add"]')
    __total_price_locator = (By.XPATH, '//div[@data-autom="bagtotalvalue" and text() = "$158.00"]')
    __quantity_check_locator = (By.XPATH, '//select[@data-autom="item-quantity-dropdown"]')
    __ten_items_locator = (By.XPATH, '//option[@value="10"]')
    __blank_click_locator = (By.XPATH, '//div[@class="rs-bag-headermessage"]')
    __final_price_locator = (By.XPATH, '//div[@data-autom="bagtotalvalue" and text()="$990.00"]')
    __expected_text = 'Your bag is empty.'

    @allure.step
    @property
    def expected_text_return(self):
        return self.__expected_text

    @allure.step
    def remove_item_from_bag(self):
        self.click(self.__remove_item_locator)

    @allure.step
    def remove_button_click(self):
        self.click(self.__remove_button_loctor_for_remove)
        return self

    @allure.step
    def is_empty_bag_got(self):
        return self.get_text(self.__emptiness_assert_locator)

    @allure.step
    def is_total_items_displayed(self):
        return self.is_displayed(self.__total_items_in_cart)

    @allure.step
    def add_apple_care(self):
        self.click(self.__add_apple_care_locator)

    @allure.step
    def is_total_price_displayed(self):
        return self.is_displayed(self.__total_price_locator)

    @allure.step
    def click_quantity_check(self):
        self.click(self.__quantity_check_locator)
        return self

    @allure.step
    def click_quantity_value(self):
        self.click(self.__ten_items_locator)
        return self

    @allure.step
    def blank_click(self):
        self.click(self.__blank_click_locator)
        return self

    @allure.step
    def is_final_price_displayed(self):
        return self.is_displayed(self.__final_price_locator)
