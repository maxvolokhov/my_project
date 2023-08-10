from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class GiftCardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __mail_locator = (By.XPATH, '//div/*[1]/label[@class="form-selector-label"]')
    __amount_locator = (By.XPATH, '//button[@data-autom="choose-amount-100"]')
    __recipient_name = (By.XPATH, '//input[@name="toName"]')
    __recipient_email = (By.XPATH, '//input[@name="toEmail"]')
    __sender_name = (By.XPATH, '//input[@name="fromName"]')
    __sender_email = (By.XPATH, '//input[@name="fromEmail"]')
    __text_to_hover = (By.XPATH, '//h2[text()="Want to add a personalized message?"]')
    __add_to_bag = (By.XPATH, '//button[@name="add-to-cart"]')
    __validate_locator = (By.XPATH, '//h1[text()="Your bag total is $100.00."]')

    def click_mail(self):
        self.click(self.__mail_locator)
        return self

    def amount_select(self):
        self.click(self.__amount_locator)
        return self

    def field_active(self):
        self.click(self.__recipient_name)
        return self

    def field_active2(self):
        self.click(self.__recipient_email)
        return self

    def field_active3(self):
        self.click(self.__sender_name)
        return self

    def field_active4(self):
        self.click(self.__sender_email)
        return self

    def set_r_name(self, apple_id_value):
        self.send_keys(self.__recipient_name, apple_id_value)
        return self

    def set_r_email(self, apple_id_value):
        self.send_keys(self.__recipient_email, apple_id_value)
        return self

    def set_s_name(self, apple_id_value):
        self.send_keys(self.__sender_name, apple_id_value)
        return self

    def set_s_email(self, apple_id_value):
        self.send_keys(self.__sender_email, apple_id_value)
        return self

    def add_to_cart(self):
        self.click(self.__add_to_bag)
        return self

    def click_for_text(self):
        self.click(self.__text_to_hover)
        return self

    def make_validate(self):
        return self.is_displayed(self.__validate_locator)
