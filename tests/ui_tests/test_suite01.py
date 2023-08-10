import os
from config_reader import Readconfig
from page_objects.apple_contact_page import AppleContactPage
from page_objects.buy_iphone_page import BuyIphonePage
from page_objects.entertainment_page import EntertainmentPage
from page_objects.language_switch_page import LanguageSwitchPage
from page_objects.main_page import MainPage
from page_objects.sign_in_page import SigninPage
import pytest


@pytest.mark.smoke
def test_page_move(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    main_page.entertainment_find_and_click()
    entertainment_page = EntertainmentPage(driver)
    apple_podcasts_page = entertainment_page.apple_podcasts_find_and_click()
    assert apple_podcasts_page.is_text_displayed(), 'Text element does not exists'


@pytest.mark.smoke
@pytest.mark.regression
def test_apple_store_id_input(create_driver):
    apple_id, password = Readconfig.get_creds()
    driver = create_driver
    main_page = MainPage(driver)
    main_page.apple_store_find_and_click()
    sign_in_page = SigninPage(driver)
    sign_in_page.frame()
    sign_in_page.set_apple_id(apple_id).login_click()
    sign_in_page.set_password(password).login_click()
    assert sign_in_page.is_text_login_displayed(), 'Text element does not exists'


@pytest.mark.regression
def test_apple_contacts(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    main_page.apple_contact()
    apple_contact_page = AppleContactPage(driver)
    assert apple_contact_page.text_country(), 'Countries elements do not exist'


@pytest.mark.smoke
def test_screen_of_buy_page(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    main_page.buy_iphone()
    buy_iphone_page = BuyIphonePage(driver)
    buy_iphone_page.new_click()
    driver.save_screenshot("screenshot.png")
    assert os.path.isfile("screenshot.png"), "Screenshot does not exist"


@pytest.mark.smoke
@pytest.mark.regression
def test_language_change(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    main_page.language_click()
    language_switch_page = LanguageSwitchPage(driver)
    italian_page = language_switch_page.italy_select()
    assert italian_page.is_word_displayed(), 'Language has not been changed to Italian'
