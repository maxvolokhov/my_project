from page_objects.air_pods2 import AirPods2Page
from page_objects.air_pods_case_page import AirPodsCasePage
from page_objects.airpods_page import AirPodsPage
from page_objects.apple_books_page import AppleBooksPage
from page_objects.apple_tv_page import AppleTvPage
import pytest


@pytest.mark.smoke
def test_airpods_item_add(air_pods_navigate):
    driver = air_pods_navigate
    airpods_page = AirPodsPage(driver)
    airpods_page.no_graving_click().add_item_to_cart().add_any_additional_item()
    bag_page = airpods_page.go_to_cart()
    assert bag_page.check_total_items(), 'Cart consists not of 2 items'


@pytest.mark.regression
def test_apple_tv_with_care(apple_tv_navigate):
    driver = apple_tv_navigate
    apple_tv_page = AppleTvPage(driver)
    apple_tv_page.wifi_version_click().put_item_in_bag()
    bag_page = apple_tv_page.click_on_proceed_button()
    bag_page.add_apple_care()
    assert bag_page.check_total_price(), 'Apple Care has not been added into cart'


@pytest.mark.smoke
@pytest.mark.regression
def test_airpods_case(air_pods_case):
    driver = air_pods_case
    air_pods_case_page = AirPodsCasePage(driver)
    air_pods_case_page.select_multicolor_case().add_to_bag_click()
    checkout_page = air_pods_case_page.checkout_move()
    checkout_page.frame()
    assert checkout_page.validate_presence(), 'Move to checkout has not been executed'


@pytest.mark.smoke
def test_airpods_increase(air_pods2):
    driver = air_pods2
    air_pods2_page = AirPods2Page(driver)
    air_pods2_page.atb_click().selector_click().value_click()
    assert air_pods2_page.price_validator(), 'Price is incorrect, items quantity has not been changed'


@pytest.mark.regression
def test_price_apple_book(apple_books_navigate):
    driver = apple_books_navigate
    apple_books_page = AppleBooksPage(driver)
    top_books_page = apple_books_page.go_to_browse_page()
    top_books_page.book_select()
    assert top_books_page.price_is_displayed(), 'Price is not located on the page'
