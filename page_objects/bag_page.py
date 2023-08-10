from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class BagPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __remove_item_locator = (By.XPATH, '''//button[@id="shoppingCart.items.
    item-24874f80-5d59-44db-8177-8969a8284a8e.delete"]''')

    __bag_check_locator = (By.XPATH, '//*[text()="Your bag is empty."]')

    __remove_button_loctor_for_remove = (By.XPATH, '//button[@data-autom="bag-item-remove-button"]')

    __emptiness_assert_locator = (By.XPATH, '//h1[@class="rs-bag-header"]')

    __total_items_in_cart = (By.XPATH, '//a[@aria-label="Shopping Bag with item count : 2"]')

    __add_apple_care_locator = (By.XPATH, '//button[@data-autom="bag-inlineattach-add"]')

    __total_price_locator = (By.XPATH, '//div[@data-autom="bagtotalvalue" and text() = "$158.00"]')

    __quantity_check_locator = (By.XPATH, '//select[@data-autom="item-quantity-dropdown"]')

    __ten_items_locator = (By.XPATH, '//option[@value="10"]')

    __blank_click_locator = (By.XPATH, '//div[@class="rs-bag-headermessage"]')

    __final_price_locator = (By.XPATH, '//div[@data-autom="bagtotalvalue" and text()="$990.00"]')

    def remove_item_from_bag(self):
        self.click(self.__remove_item_locator)

    def bag_check(self):
        return self.is_displayed(self.__bag_check_locator)

    def remove_button_click(self):
        self.click(self.__remove_button_loctor_for_remove)

    def empty_bag_assert(self):
        return self.is_displayed(self.__emptiness_assert_locator)

    def check_total_items(self):
        return self.is_displayed(self.__total_items_in_cart)

    def add_apple_care(self):
        self.click(self.__add_apple_care_locator)

    def check_total_price(self):
        return self.is_displayed(self.__total_price_locator)

    def click_quantity_check(self):
        self.click(self.__quantity_check_locator)
        return self

    def click_quantity_value(self):
        self.click(self.__ten_items_locator)
        return self

    def blank_click(self):
        self.click(self.__blank_click_locator)
        return self

    def validate_final_price(self):
        return self.is_displayed(self.__final_price_locator)
