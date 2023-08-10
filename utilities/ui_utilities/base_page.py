import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 10)

    def __wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def __wait_until_element_selected(self, locator):
        return self.__wait.until(EC.visibility_of(locator))

    def send_keys(self, locator, value, is_clear=True, press_enter=False):
        element = self.__wait_until_element_visible(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)
        if press_enter:
            element.send_keys(Keys.ENTER)

    def switch_to_frame(self, locator):
        frame_element = self.__wait_until_element_visible(locator)
        self._driver.switch_to.frame(frame_element)
        return self

    def click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def click_2(self, locator):
        self._wait_until_element_located(locator).click()

    def click_3(self, locator):
        self.__wait_until_element_selected(locator).click()

    def is_displayed(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def click_with_js(self, locator):
        time.sleep(2)
        element = self.__wait_until_element_clickable(locator)
        self._driver.execute_script("arguments[0].click();", element)

    def search_with_js(self, locator, value):
        element = self.__wait_until_element_visible(locator)
        self._driver.execute_script("arguments[0].value = arguments[1];", element, value)
        element.send_keys(Keys.ENTER)
