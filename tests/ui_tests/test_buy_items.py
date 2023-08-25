import pytest


@pytest.mark.smoke
def test_airpods_item_add(air_pods_navigate):
    air_pods_navigate.no_graving_click().add_item_to_cart().add_any_additional_item()
    bag_page = air_pods_navigate.go_to_cart()
    assert bag_page.is_total_items_displayed(), 'Cart consists not of 2 items'


@pytest.mark.regression
def test_apple_tv_with_care(apple_tv_navigate):
    apple_tv_navigate.wifi_version_click().put_item_in_bag()
    bag_page = apple_tv_navigate.click_on_proceed_button()
    bag_page.add_apple_care()
    assert bag_page.is_total_price_displayed(), 'Apple Care has not been added into cart'


@pytest.mark.smoke
@pytest.mark.regression
def test_airpods_case(air_pods_case):
    air_pods_case.select_multicolor_case().add_to_bag_click()
    checkout_page = air_pods_case.checkout_move()
    checkout_page.frame()
    assert checkout_page.is_item_presence_displayed(), 'Move to checkout has not been executed'


@pytest.mark.smoke
def test_airpods_increase(air_pods2):
    air_pods2.atb_click().selector_click().value_click()
    assert air_pods2.is_increased_price_displayed(), 'Price is incorrect, items quantity has not been changed'


@pytest.mark.regression
def test_price_apple_book(apple_books_navigate):
    top_books_page = apple_books_navigate.go_to_browse_page()
    top_books_page.book_select()
    assert top_books_page.is_price_is_displayed(), 'Price is not located on the page'
