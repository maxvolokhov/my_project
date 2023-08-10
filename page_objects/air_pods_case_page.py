from page_objects.checkout_page import CheckoutPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AirPodsCasePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __select_red_color = (By.XPATH, '//label[@data-autom="colornav-multicolor"]')
    __add_to_bag_locator = (By.XPATH, '//button[@value="add-to-cart" and text()="Add to Bag"]')
    __checkout_locator = (By.XPATH, '//button[@id="shoppingCart.actions.checkout"]')

    def select_multicolor_case(self):
        self.click(self.__select_red_color)
        return self

    def add_to_bag_click(self):
        self.click(self.__add_to_bag_locator)
        return self

    def checkout_move(self):
        self.click(self.__checkout_locator)
        return CheckoutPage(self._driver)
