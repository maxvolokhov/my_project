import pytest


@pytest.mark.smoke
def test_url(navigate_to_buy_section, env):
    navigate_to_buy_section.new_click().color_select()
    initial_url = env.buy_page_url
    updated_url = navigate_to_buy_section._driver.current_url
    assert updated_url == initial_url, "URL has been changed"


@pytest.mark.smoke
def test_buy_macbook(macbook_page):
    macbook_page.macbook_select().add_macbook_to_bag()
    shop_bag_page = macbook_page.review_bag_click()
    assert shop_bag_page.is_item_parameters_displayed(), 'Macbook and its quantity are not located on the page'
    assert shop_bag_page.expected_text_return in shop_bag_page.is_remove_item_got(), '''Remove button is not 
    located on the page'''


@pytest.mark.regression
def test_apple_watch(apple_watch_page):
    apple_watch_page.size_select().add_to_bag().add_item_to_bag()
    assert apple_watch_page.expected_item_quantity_return in apple_watch_page.is_item_quantity_got(), '''The quantity 
    of items in bag is wrong'''


@pytest.mark.smoke
@pytest.mark.regression
def test_bag_status(create_driver_main_page):
    create_driver_main_page.click_bag_locator()
    assert create_driver_main_page.expected_text_return in create_driver_main_page.is_bag_empty_got(), '''There are 
    some items in your bag'''


@pytest.mark.smoke
@pytest.mark.regression
def test_remove_from_cart(air_tag_page):
    air_tag_page.skip_engraving().add_airtag_to_bag()
    bag_page = air_tag_page.review_bag_click()
    bag_page.remove_button_click()
    assert bag_page.expected_text_return in bag_page.is_empty_bag_got(), 'Air_tag is still in your bag'
