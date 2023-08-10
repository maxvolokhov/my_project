from selenium import webdriver

CHROME = 1
SAFARI = 2
FIREFOX = 3


def create_driver_factory(driver_id):
    if int(driver_id) == CHROME:
        return webdriver.Chrome()
    elif int(driver_id) == SAFARI:
        return webdriver.Safari()
    elif int(driver_id) == FIREFOX:
        return webdriver.Firefox()
    else:
        return webdriver.Chrome()
