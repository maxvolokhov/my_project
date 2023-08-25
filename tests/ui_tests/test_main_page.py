import os
from page_objects.apple_contact_page import AppleContactPage
from page_objects.buy_iphone_page import BuyIphonePage
from page_objects.entertainment_page import EntertainmentPage
from page_objects.language_switch_page import LanguageSwitchPage
from page_objects.sign_in_page import SigninPage
import pytest


@pytest.mark.smoke
def test_page_move(navigate_to_main_page):
    navigate_to_main_page.entertainment_find_and_click()
    entertainment_page = EntertainmentPage(navigate_to_main_page._driver)
    apple_podcasts_page = entertainment_page.apple_podcasts_find_and_click()
    assert apple_podcasts_page.expected_text in apple_podcasts_page.text_presence_check(), 'Text does not exist'


@pytest.mark.smoke
@pytest.mark.regression
def test_apple_store_id_input(navigate_to_main_page, env):
    apple_id, password = env.apple_id, env.password
    navigate_to_main_page.apple_store_find_and_click()
    sign_in_page = SigninPage(navigate_to_main_page._driver)
    sign_in_page.frame()
    sign_in_page.set_apple_id(apple_id).login_click()
    sign_in_page.set_password(password).login_click()
    assert sign_in_page.is_text_login_displayed(), 'Text element does not exists'


@pytest.mark.regression
@pytest.mark.parametrize('country', AppleContactPage.countries_to_check)
def test_apple_contacts(navigate_to_main_page, country):
    navigate_to_main_page.apple_contact()
    apple_contact_page = AppleContactPage(navigate_to_main_page._driver)
    assert apple_contact_page.is_country_displayed(country), f'{country} element does not exist'


@pytest.mark.smoke
def test_screen_of_buy_page(navigate_to_main_page):
    navigate_to_main_page.buy_iphone()
    buy_iphone_page = BuyIphonePage(navigate_to_main_page._driver)
    buy_iphone_page.new_click()
    navigate_to_main_page._driver.save_screenshot("screenshot.png")
    assert os.path.isfile("screenshot.png"), "Screenshot does not exist"


@pytest.mark.smoke
@pytest.mark.regression
def test_language_change(navigate_to_main_page):
    navigate_to_main_page.language_click()
    language_switch_page = LanguageSwitchPage(navigate_to_main_page._driver)
    italian_page = language_switch_page.italy_select()
    assert italian_page.italian_text_check in italian_page.italian_word_displayed(), '''Language has not
     been changed to Italian'''
