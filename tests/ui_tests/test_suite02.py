from config_reader import Readconfig
from page_objects.air_tag_page import AirTagPage
from page_objects.apple_watch_page import AppleWatchPage
from page_objects.buy_iphone_page import BuyIphonePage
from page_objects.macbook_page import MacbookPage
from page_objects.main_page import MainPage
import pytest


@pytest.mark.smoke
def test_url(navigate_to_buy_section):
    driver = navigate_to_buy_section
    buy_iphone_page = BuyIphonePage(driver)
    buy_iphone_page.new_click().color_select()
    initial_url = Readconfig.get_buy_page()
    updated_url = driver.current_url
    assert updated_url == initial_url, "URL has been changed"


@pytest.mark.smoke
def test_buy_macbook(macbook_page):
    driver = macbook_page
    macbook_page = MacbookPage(driver)
    macbook_page.macbook_select().add_macbook_to_bag()
    shop_bag_page = macbook_page.review_bag_click()
    assert shop_bag_page.are_items_displayed(), 'Macbook and its quantity are not located on the page'
    assert shop_bag_page.remove_item_displayed(), 'Remove button is not located on the page'


@pytest.mark.regression
def test_apple_watch(apple_watch_page):
    driver = apple_watch_page
    apple_watch_page = AppleWatchPage(driver)
    apple_watch_page.size_select().add_to_bag().add_item_to_bag()
    assert apple_watch_page.item_quantity_check(), 'The quantity of items in bag is wrong'


@pytest.mark.smoke
@pytest.mark.regression
def test_bag_status(create_driver):
    driver = create_driver
    main_page = MainPage(driver)
    main_page.click_bag_locator()
    assert main_page.bag_empty_display(), 'There are some items in your bag'


@pytest.mark.smoke
@pytest.mark.regression
def test_remove_from_cart(air_tag_page):
    driver = air_tag_page
    air_tag_page = AirTagPage(driver)
    air_tag_page.skip_engraving().add_airtag_to_bag()
    bag_page = air_tag_page.review_bag_click()
    bag_page.remove_button_click()
    assert bag_page.empty_bag_assert(), 'Air_tag is still in your bag'
