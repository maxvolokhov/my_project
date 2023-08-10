from config_reader import Readconfig
from page_objects.apple_store_page import AppleStorePage
from page_objects.home_pod_page import HomePodPage
from page_objects.main_page import MainPage
from page_objects.retail_page import RetailPage
import pytest


@pytest.mark.regression
def test_apple_shop_search(create_driver):
    apple_store_name = Readconfig.get_search_input()
    driver = create_driver
    main_page = MainPage(driver)
    retail_page = main_page.store_click()
    retail_page.set_apple_store(apple_store_name).select_from_list()
    assert retail_page.store_work_time(), 'Required apple store has not been selected'


@pytest.mark.smoke
def test_retail_apple_store(retail_page_navigate):
    driver = retail_page_navigate
    retail_page = RetailPage(driver)
    retail_page.click_us_drop_down().select_austria()
    vienna_page = retail_page.austria_store_click()
    assert vienna_page.address_is_located(), 'Vienna apple sore has not been found'


@pytest.mark.smoke
@pytest.mark.regression
def test_apple_wallet(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    apple_wallet_page = main_page.go_to_wallet()
    apple_wallet_page.drop_down_click()
    support_apple_page = apple_wallet_page.learn_more_click()
    assert support_apple_page.validate_text_presence(), 'Redirect to requested page has not been executed'


@pytest.mark.smoke
def test_accessories_search(apple_store_navigate):
    search_input = Readconfig.get_accessories_search()
    driver = apple_store_navigate
    apple_sore = AppleStorePage(driver)
    apple_sore.accessories_click().insert_search_line(search_input, press_enter=True)
    assert apple_sore.validate_search_result(), 'Requested item does not exist'


@pytest.mark.regression
def test_apple_home_pod(apple_home_pod_navigate):
    driver = apple_home_pod_navigate
    home_pod_page = HomePodPage(driver)
    home_pod_page.add_homepod_to_bag()
    bag_page = home_pod_page.check_your_bag()
    bag_page.click_quantity_check().click_quantity_value().blank_click()
    assert bag_page.validate_final_price(), '10 items have not been selected'
